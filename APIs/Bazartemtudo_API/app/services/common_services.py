from app import db

def get_all(model):
    return model.query.all()

def get_by_id(model, id):
    return model.query.get(id)

def add_instance(instance):
    db.session.add(instance)
    db.session.commit()
    return instance

def update_instance():
    db.session.commit()

def delete_instance(instance):
    db.session.delete(instance)
    db.session.commit()
