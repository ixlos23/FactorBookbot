#ducker_hub: # noqa
    #sudo docker tag factorbook23-bot:latest ixlos23/name.. # noqa



#docker-compose_yml:                                                                                                                    # noqa
    # version: '3.11'                                                                                                                    # noqa
    #                                                                                                                     # noqa
    #                                                                                                                     # noqa
    # services:                                                                                                                    # noqa
    #   bot:                                                                                                                    # noqa
    #     build: .                                                                                                                    # noqa
    #     restart: always                                                                                                                    # noqa
    #     container_name: factor_book_con                                                                                                                    # noqa
    #     depends_on:                                                                                                                    # noqa
    #       - pg                                                                                                                    # noqa
    #                                                                                                                     # noqa
    #                                                                                                                     # noqa
    #   pg:                                                                                                                    # noqa
    #     image: postgres:alpine                                                                                                                    # noqa
    #     restart: always                                                                                                                    # noqa
    #     container_name: pg_con                                                                                                                    # noqa
    #     environment:                                                                                                                    # noqa
    #       POSTGRES_PASSWORD: 1                                                                                                                    # noqa
    #     ports:                                                                                                                    # noqa
    #       - "5433:5432"                                                                                                                    # noqa
    #     volumes:                                                                                                                    # noqa
    #       - pg_data:/var/lib/postgresql/data/                                                                                                                    # noqa
    #                                                                                                                     # noqa
    # volumes:                                                                                                                    # noqa
    #   pg_data:                                                                                                                    # noqa

# pg_dump:
    # sudo docker run --name pg_con -i -t -d -e POSTGRES_PASSWORD=1 -P 5433:5432 postgres:alpine
    # docker exec -it -u postgres pg_con psql
    # docker exec pga_con pg_dump _U postgres -F t postgres > test.tar
#pg_restore:
    # docker cp test.tar pg_con:/test.tar
    # docker exec -it pg_con bash
    # pg_restore -U postgres -d postgres test.tar
    # teksh: docker exec -it -u postgres pg_con psql


