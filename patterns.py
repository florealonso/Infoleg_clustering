# regex tokenizer
PATTERN = r'''(?x)
   (?:Ley\sN[ºo°]*\s\d{1,}(?:\.\d+)*)                # Leyes como entidad
   | (?:[Aa]nexo[s]?[\sIVXLCDMy,]*[IVXLCDM]+)        # anexos
   | (?:Nota[\sA-Za-z()ºo°\.]+[\d|/]+)               # Notas como entidad
   | (?:Decreto[A-Zºo°\sa-z]+[\d|/]+)                # Decretos como entidad
   | (?:[Aa]rt[ií]culo[A-Z|\sºo°]+\d+º*)             # Articulos como entidad
   | (?:[Aa]rt\.*[\s+\d+]+º*)                        # abreviacion de articulo
   | (?:Resoluci[óo]n[A-Zºo°\sa-z]+[\d/]+)           # Resoluciones como entidad
   | (?:Disposici[óo]n[A-Zºo°\sa-z]+[\d/]+)          # Disposicion como entidad
   | (?:Expediente[A-Zºo°\s]+[\d/]+)                 # Expediente como entidad
   | (?:punto\s[\d\.]+)                              # punto x.x.x. como entidad
   | (?:\d{1,2}[\sa-z]+\d{4})                        # fechas
   | (?:[A-Z][a-záéíóú]+\s[A-Z]\.\s[A-Z][a-záéíóú]+) # entidades humanas Fulano M. Mengano
   | (?:MINISTERIO[\sA-Z,]*[A-Z]+)                   # Ministerios como entidad
   | (?:REPUBLICA[\sDE]*[A-Z]+)                      # Republica como entidad
   | (?:SECRETARIA[\sA-Z,]*[A-Z]+)                   # Secretaria como entidad
   | (?:SERVICIO[\sA-Z,]*[A-Z]+)                     # Servicios como entidad
   | (?:DIRECCION[\sA-Z,]*[A-Z]+)                    # Direccion como entidad
   | \w+(?:-\w+)*                                    # palabras con '-' opcional
   | \.\.\.                                          # ...
   | [][.,;"'?():-_`]
   | (?:\d+)                                         # numeros
   | (?:[.\n])                                       # punto y aparte
'''

# regex named entity
IS_NE = r'''(?x)
   (?:Ley\sN[ºo°]*\s\d{1,}(?:\.\d+)*)                # Leyes como entidad
   | (?:Nota[\sA-Za-z()ºo°\.]+[\d|/]+)               # Notas como entidad
   | (?:Decreto[A-Zºo°\sa-z]+[\d|/]+)                # Decretos como entidad
   | (?:Resoluci[óo]n[A-Zºo°\sa-z]+[\d/]+)           # Resoluciones como entidad
   | (?:Disposici[óo]n[A-Zºo°\sa-z]+[\d/]+)          # Disposicion como entidad
   | (?:Expediente[A-Zºo°\s]+[\d/]+)                 # Expediente como entidad
   | (?:[A-Z][a-záéíóú]+\s[A-Z]\.\s[A-Z][a-záéíóú]+) # entidades humanas Fulano M. Mengano
   | (?:MINISTERIO[\sA-Z,]*[A-Z]+)                   # Ministerios como entidad
   | (?:REPUBLICA[\sDE]*[A-Z]+)                      # Republica como entidad
   | (?:SECRETARIA[\sA-Z,]*[A-Z]+)                   # Secretaria como entidad
   | (?:SERVICIO[\sA-Z,]*[A-Z]+)                     # Servicios como entidad
   | (?:DIRECCION[\sA-Z,]*[A-Z]+)                    # Direccion como entidad
'''
