GET_CHARACTERS = '''SELECT * FROM charactercreator_character;'''


CREATE_TEST_TABLE = '''
    CREATE TABLE test_table
    ("id" SERIAL NOT NULL PRIMARY KEY,
    "name"  VARCHAR(200) NOT NULL,
    "age" INT NOT NULL,
    "country_of_origin" VARCHAR(200) NOT NULL);
'''

# insert rows in th table

INSERT_TEST_TABLE = '''
    INSERT INTO test_table("name", "age", "country_of_origin")
    VALUES ('Rayn Allred', 30, 'Uganda');
'''

AVG_ITEM_WEIGHT_PER_CHARACTER = '''
    SELECT cc_char.name, SUM(ai.weight)
    FROM charactercreator_character as cc_char
    JOIN charactercreator_character_inventory as CC_inv
    ON cc_char.character_id = cc_inv.character_id
    JOIN armory_item as ai
    ON ai.item_id = cc_inv.item_id
    GROUP BY cc_char.character_id'''
