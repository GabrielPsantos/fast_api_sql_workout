CREATE TABLE item(
    item_uuid uuid DEFAULT uuid_generate_v4(),
    title VARCHAR(30) NOT NULL,
    description_body VARCHAR(30) NOT NULL,
    item_owner uuid NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    item_file_path VARCHAR NULL,
    PRIMARY KEY (item_uuid),
    CONSTRAINT fk_item_id FOREIGN KEY (item_owner) REFERENCES client (client_uuid)
);
