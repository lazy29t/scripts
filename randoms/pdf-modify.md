```
import base64
import PyPDF2

# Payload codificado en base64
encoded_payload = "powershell -s laG9sYSBjb21vIGVzdGFzCg=="

# Decodifica el payload
decoded_payload = base64.b64decode(encoded_payload).decode('utf-8')

# Ruta del archivo PDF original y modificado
pdf_original_path = 'ruta_del_archivo_original.pdf'
pdf_modified_path = 'ruta_del_archivo_modificado.pdf'

# Abre el archivo PDF original
with open(pdf_original_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_writer = PyPDF2.PdfWriter()

    # Copia las páginas del PDF original al PDF modificado
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    # Agrega el contenido del payload como un nuevo campo de formulario en la última página
    pdf_writer.updatePageFormFieldValues(0, {'payload_field': [decoded_payload]})

    # Guarda el PDF modificado en un nuevo archivo
    with open(pdf_modified_path, 'wb') as modified_pdf_file:
        pdf_writer.write(modified_pdf_file)

print("PDF modificado creado en:", pdf_modified_path)
```

----

```bash
Traceback (most recent call last):
  File "/home/dp4ud/Desktop/tools/own/pdf-modify.py", line 8, in <module>
    decoded_payload = base64.b64decode(encoded_payload).decode('utf-8')
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/base64.py", line 88, in b64decode
    return binascii.a2b_base64(s, strict_mode=validate)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
binascii.Error: Invalid base64-encoded string: number of data characters (1377) cannot be 1 more than a multiple of 4
```
