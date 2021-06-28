CREATE TABLE client(
    client_uuid uuid DEFAULT uuid_generate_v4(),
    client_email VARCHAR(25) NOT NULL,
    hashed_password VARCHAR(250) NOT NULL,
    client_photo_profile VARCHAR NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (client_uuid)
);