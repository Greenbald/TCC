--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.1
-- Dumped by pg_dump version 9.4.1
-- Started on 2016-09-26 19:49:06

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 180 (class 3079 OID 11855)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2039 (class 0 OID 0)
-- Dependencies: 180
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 177 (class 1259 OID 57542)
-- Name: Hashtag; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "Hashtag" (
    text character varying(40),
    count integer DEFAULT 1 NOT NULL,
    id bigint NOT NULL
);


ALTER TABLE "Hashtag" OWNER TO postgres;

--
-- TOC entry 2040 (class 0 OID 0)
-- Dependencies: 177
-- Name: TABLE "Hashtag"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE "Hashtag" IS 'Every row is an hashtag';


--
-- TOC entry 2041 (class 0 OID 0)
-- Dependencies: 177
-- Name: COLUMN "Hashtag".count; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "Hashtag".count IS 'The number of times this hashtag appear';


--
-- TOC entry 179 (class 1259 OID 57619)
-- Name: Hashtag_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Hashtag_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Hashtag_id_seq" OWNER TO postgres;

--
-- TOC entry 2042 (class 0 OID 0)
-- Dependencies: 179
-- Name: Hashtag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Hashtag_id_seq" OWNED BY "Hashtag".id;


--
-- TOC entry 176 (class 1259 OID 41126)
-- Name: Tweet; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "Tweet" (
    id bigint NOT NULL,
    t_id bigint NOT NULL,
    created_at character varying(35) NOT NULL,
    u_id bigint NOT NULL,
    text text NOT NULL,
    source character varying(11) NOT NULL,
    raw_text text NOT NULL
);


ALTER TABLE "Tweet" OWNER TO postgres;

--
-- TOC entry 2043 (class 0 OID 0)
-- Dependencies: 176
-- Name: TABLE "Tweet"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE "Tweet" IS 'The representation of the tweet''s data';


--
-- TOC entry 2044 (class 0 OID 0)
-- Dependencies: 176
-- Name: COLUMN "Tweet".t_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "Tweet".t_id IS 'The tweet''s id from given from twitter';


--
-- TOC entry 2045 (class 0 OID 0)
-- Dependencies: 176
-- Name: COLUMN "Tweet".created_at; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "Tweet".created_at IS 'The moment of the day the tweet was created(Manha, tarde, noite, madrugada)';


--
-- TOC entry 2046 (class 0 OID 0)
-- Dependencies: 176
-- Name: COLUMN "Tweet".u_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "Tweet".u_id IS 'User id that correlates with the User table';


--
-- TOC entry 2047 (class 0 OID 0)
-- Dependencies: 176
-- Name: COLUMN "Tweet".source; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "Tweet".source IS 'the device the tweet was posted';


--
-- TOC entry 2048 (class 0 OID 0)
-- Dependencies: 176
-- Name: COLUMN "Tweet".raw_text; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "Tweet".raw_text IS 'The tweet text without any entity(e.g., hashtags, symbols, user_mentions and urls)';


--
-- TOC entry 178 (class 1259 OID 57553)
-- Name: Tweet_Hashtag; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "Tweet_Hashtag" (
    t_id bigint NOT NULL,
    h_id bigint NOT NULL
);


ALTER TABLE "Tweet_Hashtag" OWNER TO postgres;

--
-- TOC entry 2049 (class 0 OID 0)
-- Dependencies: 178
-- Name: TABLE "Tweet_Hashtag"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE "Tweet_Hashtag" IS 'The table that represents the relationship of a tweet with hashtags';


--
-- TOC entry 2050 (class 0 OID 0)
-- Dependencies: 178
-- Name: COLUMN "Tweet_Hashtag".t_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "Tweet_Hashtag".t_id IS 'The id of the tweet';


--
-- TOC entry 174 (class 1259 OID 41122)
-- Name: Tweet_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Tweet_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Tweet_id_seq" OWNER TO postgres;

--
-- TOC entry 2051 (class 0 OID 0)
-- Dependencies: 174
-- Name: Tweet_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Tweet_id_seq" OWNED BY "Tweet".id;


--
-- TOC entry 175 (class 1259 OID 41124)
-- Name: Tweet_u_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "Tweet_u_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "Tweet_u_id_seq" OWNER TO postgres;

--
-- TOC entry 2052 (class 0 OID 0)
-- Dependencies: 175
-- Name: Tweet_u_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "Tweet_u_id_seq" OWNED BY "Tweet".u_id;


--
-- TOC entry 173 (class 1259 OID 41115)
-- Name: User; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "User" (
    friends_count integer NOT NULL,
    description text,
    location character varying(100),
    followers_count integer NOT NULL,
    id bigint NOT NULL,
    u_id bigint NOT NULL
);


ALTER TABLE "User" OWNER TO postgres;

--
-- TOC entry 2053 (class 0 OID 0)
-- Dependencies: 173
-- Name: TABLE "User"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE "User" IS 'This table represents the data associated to a specific user who posted a specific tweet';


--
-- TOC entry 2054 (class 0 OID 0)
-- Dependencies: 173
-- Name: COLUMN "User".friends_count; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "User".friends_count IS 'The number of double sided connections in your twitter''s account, i.e., if you have a friend A in which you follow, if this friend follow you back, this is considered a friendship.';


--
-- TOC entry 2055 (class 0 OID 0)
-- Dependencies: 173
-- Name: COLUMN "User".description; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "User".description IS 'Description uf tweet''s user';


--
-- TOC entry 2056 (class 0 OID 0)
-- Dependencies: 173
-- Name: COLUMN "User".followers_count; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "User".followers_count IS 'The number of followers of this user';


--
-- TOC entry 2057 (class 0 OID 0)
-- Dependencies: 173
-- Name: COLUMN "User".u_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "User".u_id IS 'User id given from twitter''s api';


--
-- TOC entry 172 (class 1259 OID 41113)
-- Name: User_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE "User_id_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE "User_id_seq" OWNER TO postgres;

--
-- TOC entry 2058 (class 0 OID 0)
-- Dependencies: 172
-- Name: User_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "User_id_seq" OWNED BY "User".id;


--
-- TOC entry 1904 (class 2604 OID 57621)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Hashtag" ALTER COLUMN id SET DEFAULT nextval('"Hashtag_id_seq"'::regclass);


--
-- TOC entry 1902 (class 2604 OID 41129)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Tweet" ALTER COLUMN id SET DEFAULT nextval('"Tweet_id_seq"'::regclass);


--
-- TOC entry 1903 (class 2604 OID 41130)
-- Name: u_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Tweet" ALTER COLUMN u_id SET DEFAULT nextval('"Tweet_u_id_seq"'::regclass);


--
-- TOC entry 1901 (class 2604 OID 41118)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "User" ALTER COLUMN id SET DEFAULT nextval('"User_id_seq"'::regclass);


--
-- TOC entry 1915 (class 2606 OID 57627)
-- Name: Hashtag_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Hashtag"
    ADD CONSTRAINT "Hashtag_pkey" PRIMARY KEY (id);


--
-- TOC entry 1917 (class 2606 OID 57589)
-- Name: Hashtag_text_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Hashtag"
    ADD CONSTRAINT "Hashtag_text_key" UNIQUE (text);


--
-- TOC entry 1919 (class 2606 OID 57557)
-- Name: Tweet_Hashtag_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Tweet_Hashtag"
    ADD CONSTRAINT "Tweet_Hashtag_pkey" PRIMARY KEY (t_id, h_id);


--
-- TOC entry 1911 (class 2606 OID 41144)
-- Name: Tweet_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Tweet"
    ADD CONSTRAINT "Tweet_pkey" PRIMARY KEY (id);


--
-- TOC entry 1913 (class 2606 OID 41154)
-- Name: Tweet_t_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Tweet"
    ADD CONSTRAINT "Tweet_t_id_key" UNIQUE (t_id);


--
-- TOC entry 1907 (class 2606 OID 41157)
-- Name: User_u_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "User"
    ADD CONSTRAINT "User_u_id_key" UNIQUE (u_id);


--
-- TOC entry 1909 (class 2606 OID 41138)
-- Name: id; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "User"
    ADD CONSTRAINT id PRIMARY KEY (id);


--
-- TOC entry 1922 (class 2606 OID 57628)
-- Name: Tweet_Hashtag_h_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Tweet_Hashtag"
    ADD CONSTRAINT "Tweet_Hashtag_h_id_fkey" FOREIGN KEY (h_id) REFERENCES "Hashtag"(id);


--
-- TOC entry 1921 (class 2606 OID 57563)
-- Name: Tweet_Hashtag_t_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Tweet_Hashtag"
    ADD CONSTRAINT "Tweet_Hashtag_t_id_fkey" FOREIGN KEY (t_id) REFERENCES "Tweet"(id);


--
-- TOC entry 1920 (class 2606 OID 41158)
-- Name: Tweet_u_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Tweet"
    ADD CONSTRAINT "Tweet_u_id_fkey" FOREIGN KEY (u_id) REFERENCES "User"(u_id);


--
-- TOC entry 2038 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2016-09-26 19:49:06

--
-- PostgreSQL database dump complete
--

