def imprimir_encabezado(texto):
            """
            Imprime un encabezado formateado.

            Args:
                texto (str): Texto a mostrar en el encabezado.
            """
            print("\n" + "=" * 50)
            print(f"{texto:^50}")
            print("=" * 50)
            
            
def validar_entrada(mensaje, tipo):
    while True:
        entrada = input(mensaje) 
        if tipo == "num" and entrada.isdigit():
            return int(entrada)
        elif tipo == "str" and not entrada.isdigit():
            return entrada.title().strip()
        else:
            notificacion = f"Solo se aceptan {('números enteros' if tipo == 'num' else 'texto')}"
            print(notificacion)
            
            