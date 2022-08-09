CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    make TEXT,
    model TEXT,
    owner_first VARCHAR(30),
    owner_last VARCHAR(30),
    active BOOLEAN DEFAULT 1
);

INSERT INTO vehicle (
    make,
    model,
    owner_first,
    owner_last
) Values (
    "Honda",
    "Accord",
    "DeVonte",
    "Gray"
);

INSERT INTO vehicle (
    make,
    model,
    owner_first,
    owner_last
) Values (
    "Ford",
    "Mustang",
    "Jason",
    "Bourne"
);

INSERT INTO vehicle (
    make,
    model,
    owner_first,
    owner_last
) Values (
    "Honda",
    "Accord",
    "John",
    "Wick"
);

INSERT INTO vehicle (
    make,
    model,
    owner_first,
    owner_last
) Values (
    "Chevy",
    "Impala",
    "Keanu",
    "Reeves"
);
