#!/usr/bin/env bash
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/db
psql -a -d $DATABASE_URL -f db.sql