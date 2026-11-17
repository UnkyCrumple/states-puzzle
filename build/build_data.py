"""Build puzzle-tile geometry for the four map eras from poezn/us-history-maps GeoJSON.

Usage: python3 -I build_data.py  (reads SRC, writes OUT/levels.json)
"""
import json, math, sys
import numpy as np
import shapely
from shapely.geometry import shape, box
from shapely.ops import unary_union

SRC = '/home/claude/poezn/us-history-maps/GeoJSON/'
OUT = '/home/claude/data/out/levels.json'

# Albers equal-area conic (USGS "contiguous" parameters), output in km, y up
R = 6371.0
LON0, LAT0, P1, P2 = -96.0, 37.5, 29.5, 45.5
_n = (math.sin(math.radians(P1)) + math.sin(math.radians(P2))) / 2
_C = math.cos(math.radians(P1)) ** 2 + 2 * _n * math.sin(math.radians(P1))
_rho0 = R * math.sqrt(_C - 2 * _n * math.sin(math.radians(LAT0))) / _n


def albers(xy):
    lon = np.radians(xy[:, 0]); lat = np.radians(xy[:, 1])
    rho = R * np.sqrt(_C - 2 * _n * np.sin(lat)) / _n
    th = _n * (lon - math.radians(LON0))
    x = rho * np.sin(th)
    y = _rho0 - rho * np.cos(th)
    return np.column_stack([x, -y])  # flip y for SVG (south = +y)


def load(fn):
    d = json.load(open(SRC + fn))
    out = []
    for f in d['features']:
        p = f['properties']
        g = shape(f['geometry'])
        if not g.is_valid:
            g = g.buffer(0)
        out.append(dict(label=p.get('LABEL'), cat=p.get('CATEGORY'), state=p.get('STATE'), geom=g))
    return out


def project(g):
    return shapely.transform(g, albers)


def is_far(label):
    return any(k in (label or '') for k in ('Alaska', 'Hawaii', 'Hawaiian', 'Russian America'))


# ---- Level definitions ------------------------------------------------------
# role: tile = draggable piece; fixed = pre-placed grey piece inside the silhouette;
#       context = faint surrounding land (other countries / unclaimed)
LEVELS = [
    dict(id='colonies', file='1789030.geojson', tiles_cat={'state'}, fixed_labels={
        'Vermont Republic', 'Disputed between Massachusetts and Colony of New Brunswick', 'Eerie Triangle'},
        tol_km=6),
    dict(id='louisiana', file='1803040.geojson', tiles_cat={'state', 'territory'}, fixed_labels={
        'D.C.', 'Disputed between Massachusetts and Colony of New Brunswick',
        'Disputed between United States and West Florida', "Disputed between Northwest Territory and Rupert's Land"},
        tol_km=9),
    dict(id='mexican', file='1848080.geojson', tiles_cat={'state', 'territory'}, fixed_labels={'D.C.'}, tol_km=12),
    dict(id='today', file='1912080.geojson', tiles_cat={'state'}, fixed_labels={'D.C.'}, tol_km=12),
]


def main():
    levels = []
    for L in LEVELS:
        feats = [f for f in load(L['file']) if not is_far(f['label'])]
        for f in feats:
            f['geom'] = project(f['geom'])
        # role assignment
        for f in feats:
            if f['label'] in L['fixed_labels']:
                f['role'] = 'fixed'
            elif f['cat'] in L['tiles_cat']:
                f['role'] = 'tile'
            else:
                f['role'] = 'context'
        # level-specific adjustments
        if L['id'] == 'colonies':
            # US-claimed western land is context, not a colony tile
            for f in feats:
                if f['label'] in ('Unorganized territory',):
                    f['role'] = 'context'
        # The silhouette bounds drive the viewport
        sil = unary_union([f['geom'] for f in feats if f['role'] in ('tile', 'fixed')])
        minx, miny, maxx, maxy = sil.bounds
        w, h = maxx - minx, maxy - miny
        cx, cy = (minx + maxx) / 2, (miny + maxy) / 2
        aspect = 4 / 3
        pad = 1.18
        vw = max(w * pad, h * pad * aspect)
        vh = vw / aspect
        vx, vy = cx - vw / 2, cy - vh / 2
        scale = 1000.0 / vw  # svg units per km

        # coverage-simplify all polygons together so shared borders stay consistent
        geoms = [f['geom'] for f in feats]
        simp = shapely.coverage_simplify(geoms, L['tol_km'])
        for f, g in zip(feats, simp):
            f['geom'] = g

        view = box(vx - 50, vy - 50, vx + vw + 50, vy + vh + 50)
        pieces = []
        for f in feats:
            g = f['geom']
            if f['role'] == 'context':
                g = g.intersection(view)
            if g.is_empty:
                continue
            pieces.append(dict(f, geom=g))

        def to_path(g):
            polys = [g] if g.geom_type == 'Polygon' else [p for p in getattr(g, 'geoms', []) if p.geom_type == 'Polygon']
            d = []
            for p in polys:
                for ring in [p.exterior] + list(p.interiors):
                    pts = [((x - vx) * scale, (y - vy) * scale) for x, y in ring.coords]
                    d.append('M' + 'L'.join(f'{a:.1f},{b:.1f}' for a, b in pts[:-1]) + 'Z')
            return ''.join(d)

        out_pieces = []
        for f in pieces:
            g = f['geom']
            bx0, by0, bx1, by1 = g.bounds
            rp = g.representative_point()
            c = g.centroid
            out_pieces.append(dict(
                label=f['label'], role=f['role'], cat=f['cat'], abbr=f['state'],
                d=to_path(g),
                bbox=[round((bx0 - vx) * scale, 1), round((by0 - vy) * scale, 1),
                      round((bx1 - vx) * scale, 1), round((by1 - vy) * scale, 1)],
                label_pt=[round((rp.x - vx) * scale, 1), round((rp.y - vy) * scale, 1)],
                area_km2=round(g.area),
            ))
        levels.append(dict(id=L['id'], source_file=L['file'], vb=[0, 0, 1000, round(1000 / aspect, 1)],
                           km_per_unit=round(1 / scale, 3), pieces=out_pieces))
        print(L['id'], len(out_pieces), 'pieces;', sum(p['role'] == 'tile' for p in out_pieces), 'tiles;',
              'km/unit', round(1 / scale, 2), 'bytes', sum(len(p['d']) for p in out_pieces))
    json.dump(levels, open(OUT, 'w'))
    for L in levels:
        print('--', L['id'])
        for p in L['pieces']:
            if p['role'] != 'context':
                w = p['bbox'][2] - p['bbox'][0]; h = p['bbox'][3] - p['bbox'][1]
                print(f"   {p['role']:5} {p['label']:<55} {w:6.0f}x{h:<6.0f} {len(p['d'])}")


main()
