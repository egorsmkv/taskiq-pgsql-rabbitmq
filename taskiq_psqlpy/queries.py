CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS {} (
    task_id {} UNIQUE,
    execution_time FLOAT,
    is_err BOOLEAN,
    error BYTEA,
    labels BYTEA,
    return_value BYTEA
)
"""

CREATE_INDEX_QUERY = """
CREATE INDEX IF NOT EXISTS {}_task_id_idx ON {} USING HASH (task_id)
"""

INSERT_RESULT_QUERY = """
INSERT INTO {} VALUES ($1, $2, $3, $4, $5, $6)
"""

IS_RESULT_EXISTS_QUERY = """
SELECT EXISTS(
    SELECT 1 FROM {} WHERE task_id = $1
)
"""

SELECT_RESULT_QUERY = """
SELECT execution_time, is_err, error, labels, return_value FROM {} WHERE task_id = $1
"""

DELETE_RESULT_QUERY = """
DELETE FROM {} WHERE task_id = $1
"""
