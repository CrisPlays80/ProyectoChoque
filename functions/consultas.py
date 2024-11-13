class Consultas:
    def __init__(self, conexion):
        self.conexion = conexion    
    def guardar_en_db(self, query, parametros):
        """
        Ejecuta una consulta SQL para insertar un nuevo registro en la base de datos.

        query: La consulta SQL de tipo INSERT.
        parametros: Una tupla con los valores que se insertarán en la base de datos.
        """
        try:
            cursor = self.conexion.cursor()
            cursor.execute(query, parametros)
            self.conexion.commit()
            return cursor.lastrowid
            print("Registro guardado correctamente")
        except Exception as e:
            print(f"Error al guardar en la base de datos: {e}")
        finally:
            cursor.close()
            
    def actualizar_registro_en_db(self, query, parametros):
        """
        Ejecuta una consulta SQL para actualizar un registro existente en la base de datos.

        query: La consulta SQL de tipo UPDATE.
        parametros: Una tupla con los nuevos valores y el ID o condición para identificar el registro.
        """
        try:
            cursor = self.conexion.cursor()
            cursor.execute(query, parametros)
            self.conexion.commit()
            print("Registro actualizado correctamente")
        except Exception as e:
            print(f"Error al actualizar el registro: {e}")
        finally:
            cursor.close()
            
    def eliminar_de_db(self, query, parametros):
        """
        Ejecuta una consulta SQL para eliminar un registro de la base de datos.

        query: La consulta SQL de tipo DELETE.
        parametros: Una tupla con el ID o la condición que identifica el registro a eliminar.
        """
        try:
            cursor = self.conexion.cursor()
            cursor.execute(query, parametros)
            self.conexion.commit()
            print("Registro eliminado correctamente")
        except Exception as e:
            print(f"Error al eliminar el registro: {e}")
        finally:
            cursor.close()
