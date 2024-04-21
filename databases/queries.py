GET_CHARACTERS = '''SELECT character_id, name FROM charactercreator_character;'''


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