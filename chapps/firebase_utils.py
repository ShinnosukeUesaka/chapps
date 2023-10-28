import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("chapps/firebase_auth.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def add_or_get_user(name):
    docs = db.collection('users').where('name', '==', name).stream()
    for doc in docs:
        return doc.to_dict()

    doc_ref = db.collection('users').document()
    doc_ref.set({
        'id': doc_ref.id,
        'name': name,
    })
    return doc_ref.get().to_dict()
