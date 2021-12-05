from flask.cli import FlaskGroup
# import project.dados as d
from project.dados import app, db, Dados, DadosSchema


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
    # d.process_file()
