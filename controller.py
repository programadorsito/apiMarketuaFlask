datos=[]

def save(data):
    if not data:return False
    datos.append(data)
    return True

def get(identificador):
    if not identificador:return None
    for d in datos:
        if d["id"]==identificador:
            return d

def update(data):
    if not data:return False
    for d in datos:
        if d["id"]==data["id"]:
            d.update(data)
    return True

def delete(identificador):
    i=0
    encontrado=False
    for d in datos:
        if identificador==d["id"]:
            encontrado=True
            break
        i+=1
    if encontrado:
        del datos[i]
        return True
    return False