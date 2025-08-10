CREATE TABLE itemstatus (
    item_type TEXT NOT NULL,
    item_id INTEGER NOT NULL,
    status TEXT NOT NULL,
    PRIMARY KEY (item_type, item_id)
);
