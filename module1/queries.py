

TOTAL_CHARACTERS = '''SELECT count(*) FROM charactercreator_character;'''

TOTAL_SUBCLASS = '''SELECT count(*) FROM charactercreator_necromancer;'''

DISTINCT_CHARACTER_NAMES = '''
    SELECT COUNT(DISTINCT name) AS distinct_names
    FROM charactercreator_character;
'''

TOTAL_ITEMS = '''SELECT COUNT(*) from armory_item'''

WEAPONS = '''SELECT count(*)
FROM armory_weapon as aw
INNER JOIN armory_item as ai
WHERE ai.item_id = aw.item_ptr_id;
'''

NON_WEAPONS = '''SELECT count(*)
from armory_item as ai
left join armory_weapon as aw
on ai.item_id = aw.item_ptr_id
where aw.power is NULL;
'''

CHARACTER_ITEMS = '''SELECT name, count(item_id)
from charactercreator_character as cc_char
inner join charactercreator_character_inventory as cc_inv
on cc_char.character_id = cc_inv.character_id
GROUP by cc_char.character_id
LIMIT 20;
'''

CHARACTER_WEAPONS = '''select cc_char.name, count(ai.item_id) as total_weapons
from armory_item as ai
INNER join armory_weapon as aw
on ai.item_id = aw.item_ptr_id
-- 37 weapons
inner join charactercreator_character_inventory as cc_inv
on ai.item_id = cc_inv.item_id
--203 weapons
INNER JOIN charactercreator_character as cc_char
on cc_char.character_id = cc_inv.character_id
group by cc_char.character_id
Limit 20;
'''

AVG_CHARACTER_ITEMS = '''select avg(total_items) as average_items_per_char FROM
(SELECT name, count(item_id) as total_items
from charactercreator_character as cc_char
inner join charactercreator_character_inventory as cc_inv
on cc_char.character_id = cc_inv.character_id
GROUP by cc_char.character_id);
'''

AVG_CHARACTER_WEAPONS = '''select avg(total_weapons) FROM
(select cc_char.name, count(ai.item_id) as total_weapons
from armory_item as ai
INNER join armory_weapon as aw
on ai.item_id = aw.item_ptr_id
-- 37 weapons
inner join charactercreator_character_inventory as cc_inv
on ai.item_id = cc_inv.item_id
--203 weapons
INNER JOIN charactercreator_character as cc_char
on cc_char.character_id = cc_inv.character_id
group by cc_char.character_id);
'''

QUERY_LIST = [TOTAL_CHARACTERS, TOTAL_SUBCLASS, DISTINCT_CHARACTER_NAMES, TOTAL_ITEMS, WEAPONS,
              NON_WEAPONS, CHARACTER_ITEMS, CHARACTER_WEAPONS, AVG_CHARACTER_ITEMS,
              AVG_CHARACTER_WEAPONS]
