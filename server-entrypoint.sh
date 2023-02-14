#!/bin/sh

uvicorn server.main:app --host=$HOST --port=$PORT