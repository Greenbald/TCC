--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.1
-- Dumped by pg_dump version 9.4.1
-- Started on 2016-09-22 13:42:19

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 177 (class 3079 OID 11855)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2019 (class 0 OID 0)
-- Dependencies: 177
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 176 (class 1259 OID 41126)
-- Name: Tweet; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE "Tweet" (
    id bigint NOT NULL,
    t_id bigint NOT NULL,
    created_at character varying(35) NOT NULL,
    u_id bigint NOT NULL,
    text text NOT NULL
);


ALTER TABLE "Tweet" OWNER TO postgres;

--
-- TOC entry 2020 (class 0 OID 0)
-- Dependencies: 176
-- Name: TABLE "Tweet"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE "Tweet" IS 'The representation of the tweet''s data';


--
-- TOC entry 2021 (class 0 OID 0)
-- Dependencies: 176
-- Name: COLUMN "Tweet".t_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "Tweet".t_id IS 'The tweet''s id from given from twitter';


--
-- TOC entry 2022 (class 0 OID 0)
-- Dependencies: 176
-- Name: COLUMN "Tweet".created_at; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "Tweet".created_at IS 'The moment of the day the tweet was created(Manha, tarde, noite, madrugada)';


--
-- TOC entry 2023 (class 0 OID 0)
-- Dependencies: 176
-- Name: COLUMN "Tweet".u_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "Tweet".u_id IS 'User id that correlates with the User table';


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
-- TOC entry 2024 (class 0 OID 0)
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
-- TOC entry 2025 (class 0 OID 0)
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
    location character varying(60),
    followers_count integer NOT NULL,
    id bigint NOT NULL,
    u_id bigint NOT NULL
);


ALTER TABLE "User" OWNER TO postgres;

--
-- TOC entry 2026 (class 0 OID 0)
-- Dependencies: 173
-- Name: TABLE "User"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE "User" IS 'This table represents the data associated to a specific user who posted a specific tweet';


--
-- TOC entry 2027 (class 0 OID 0)
-- Dependencies: 173
-- Name: COLUMN "User".friends_count; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "User".friends_count IS 'The number of double sided connections in your twitter''s account, i.e., if you have a friend A in which you follow, if this friend follow you back, this is considered a friendship.';


--
-- TOC entry 2028 (class 0 OID 0)
-- Dependencies: 173
-- Name: COLUMN "User".description; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "User".description IS 'Description uf tweet''s user';


--
-- TOC entry 2029 (class 0 OID 0)
-- Dependencies: 173
-- Name: COLUMN "User".followers_count; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN "User".followers_count IS 'The number of followers of this user';


--
-- TOC entry 2030 (class 0 OID 0)
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
-- TOC entry 2031 (class 0 OID 0)
-- Dependencies: 172
-- Name: User_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE "User_id_seq" OWNED BY "User".id;


--
-- TOC entry 1892 (class 2604 OID 41129)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Tweet" ALTER COLUMN id SET DEFAULT nextval('"Tweet_id_seq"'::regclass);


--
-- TOC entry 1893 (class 2604 OID 41130)
-- Name: u_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Tweet" ALTER COLUMN u_id SET DEFAULT nextval('"Tweet_u_id_seq"'::regclass);


--
-- TOC entry 1891 (class 2604 OID 41118)
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "User" ALTER COLUMN id SET DEFAULT nextval('"User_id_seq"'::regclass);


--
-- TOC entry 1899 (class 2606 OID 41144)
-- Name: Tweet_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Tweet"
    ADD CONSTRAINT "Tweet_pkey" PRIMARY KEY (id);


--
-- TOC entry 1901 (class 2606 OID 41154)
-- Name: Tweet_t_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "Tweet"
    ADD CONSTRAINT "Tweet_t_id_key" UNIQUE (t_id);


--
-- TOC entry 1895 (class 2606 OID 41157)
-- Name: User_u_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "User"
    ADD CONSTRAINT "User_u_id_key" UNIQUE (u_id);


--
-- TOC entry 1897 (class 2606 OID 41138)
-- Name: id; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY "User"
    ADD CONSTRAINT id PRIMARY KEY (id);


--
-- TOC entry 1902 (class 2606 OID 41158)
-- Name: Tweet_u_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY "Tweet"
    ADD CONSTRAINT "Tweet_u_id_fkey" FOREIGN KEY (u_id) REFERENCES "User"(u_id);


--
-- TOC entry 2018 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2016-09-22 13:42:20

--
-- PostgreSQL database dump complete
--

