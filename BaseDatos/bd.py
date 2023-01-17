import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='mateo',
    password='admin',
    database='prueba'
)

cursor = midb.cursor()
#------Listar datos-----
# cursor.execute('select * from Usuario')
# resultado = cursor.fetchall()
# print(resultado)

cursor.execute('select * from Usuario limit 1')
resultado = cursor.fetchall()
print(resultado)

# sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)'
# values =  ('mateo@correo.com', 'probandousuario', 21)

#----ver definiciones de tablas------
# cursor.execute('show create table Usuario')

# -----Insertar datos-------
# cursor.execute(sql,values)
# midb.commit()

# print(cursor.rowcount)
#----Actualizar datos-------
# sql = 'update Usuario set email = %s where id = %s '
# values = ( 'micorreo@correo.com', 4)
# cursor.execute(sql,values)
# midb.commit()

#-----Eliminar datos-----
# sql = 'delete from Usuario where id = %s'
# values = (4, )
# cursor.execute(sql,values)
# midb.commit()



# print(resultado)


