
CREATE TABLE IF NOT EXISTS crawler_control
 (
        handle text,
        source varchar(20),
        start_date TIMESTAMPTZ,
        last_update TIMESTAMPTZ,
        priority NUMERIC,
        status varchar(20)
    );

CREATE UNIQUE INDEX idx_crawler_control ON crawler_control(handle);


CREATE TABLE IF NOT EXISTS raw_messages
 (
        id serial,
        timeline TIMESTAMPTZ,
        handle text,
        source varchar(20),
        raw_message json,
        raw_message_text text,
        status varchar(20)
    );

SELECT create_hypertable('raw_messages', 'timeline');
CREATE UNIQUE INDEX idx_raw_messages ON raw_messages(id,timeline);


CREATE TABLE IF NOT EXISTS processed_sentiments
 (
        id int NOT NULL,
        timeline TIMESTAMPTZ,
        source varchar(20),
        message text,
        label text, -- reconsider this if needs to be array\json
        score numeric,
        symbol text[]
    );

SELECT create_hypertable('processed_sentiments', 'timeline');
CREATE UNIQUE INDEX idx_processed_sentiments ON processed_sentiments(id,timeline);
