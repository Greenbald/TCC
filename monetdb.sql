create table tweet_tokens (t_id bigint, text VARCHAR(150), classification BOOLEAN);
create table user_tokens(u_id bigint, classification BOOLEAN);
create index index_t on tweet_tokens(t_id);
create index index_u on user_tokens(u_id);