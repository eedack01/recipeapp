DROP TABLE IF EXISTS recipes;

CREATE TABLE recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text not null,
    cookingtime int NOT NULL,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL
);
