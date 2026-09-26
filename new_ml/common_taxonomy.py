"""Broad categories are labels, not proof of origin, handmade status, or composition."""
COMMON={'diya':'lighting','saree':'textiles','fabric':'textiles','handwoven_fabric':'textiles','handwoven_textile':'textiles',
 'pottery':'pottery','woodcraft':'woodcraft','metal_homeware':'metal_homeware','basket':'baskets','textile_bag':'bags','wall_hanging':'home_decor'}
FAMILIES={
 'clay_pot':'pottery','clay_diya':'lighting','bankura_horse':'pottery','jaipur_blue_pottery':'pottery',
 'channapatna':'woodcraft','kondapalli':'woodcraft','saharanpur_carving':'woodcraft','kathputli':'home_decor',
 'bamboo_basket':'baskets','sitalpati':'natural_fibre_craft','jute_craft':'natural_fibre_craft','sikkim_cane_furniture':'furniture',
 'dhokra':'metal_craft','moradabad_brassware':'metal_homeware','aranmula_kannadi':'metal_craft','kansa_vessel':'metal_homeware',
}
def describe_type(kind):
 common=kind in COMMON
 return {'category_family':COMMON[kind] if common else FAMILIES.get(kind,'textiles'),
  'product_category':kind if common else {'clay_pot':'pot','clay_diya':'diya','bamboo_basket':'basket','kansa_vessel':'vessel','aranmula_kannadi':'mirror'}.get(kind,'unspecified'),
  'craft_tradition':None if common or kind in {'clay_pot','clay_diya','bamboo_basket','jute_craft'} else kind,
  'weaving_label':'handwoven' if kind in {'handwoven_fabric','handwoven_textile'} else 'not_established'}
