# Datos del negocio
nombre_del_negocio = "Kixpoint"
direccion_del_negocio = "Don Bosco 755, San Isidro"
mail_del_negocio = "ventas@kixpoint.com"
cuit_del_negocio = "30-66479948-6"
telefono_del_negocio = "011-6969-4321"

# Bienvenida
print("¡Bienvenido a Kixpoint!")
print("Por cualquier duda o consulta, no dude en contactarnos a", mail_del_negocio, "o al teléfono", telefono_del_negocio)

# Datos del cliente
nombre_del_cliente = input("Por favor, ingrese su nombre y apellido: ").title()
dni_del_cliente = input("Por favor, ingrese su DNI: ")
mail_del_cliente = input("Por favor, ingrese su correo electrónico: ").lower()
cliente_esta_en_caba = input("¿Vive en CABA? (si/no): ").lower()
cliente_esta_en_gba = input("¿Vive en GBA? (si/no): ").lower()
cliente_esta_en_bs_as = input("¿Vive en Provincia de Buenos Aires? (si/no): ").lower()
cliente_esta_en_arg = input("¿Vive en Argentina? (si/no): ").lower()
barrio_del_cliente = input("Por favor, ingrese su barrio: ").title()
calle_y_num_del_cliente = input("Por favor, ingrese su calle y número: ").title()

### Compra
finalizarcompra = False
num_de_compras = 0
precio_de_la_compra = 0

### Catálogo de productos
nike_air_max_t_39 = 0
nike_air_max_t_41 = 0
adidas_ultraboost_t_39 = 0
adidas_ultraboost_t_41 = 0
puma_rsx_t_39 = 0
puma_rsx_t_41 = 0

vans_old_skool_t_39 = 0
vans_old_skool_t_41 = 0
converse_all_star_t_39 = 0
converse_all_star_t_41 = 0
converse_jack_purcell_t_39 = 0
converse_jack_purcell_t_41 = 0

while finalizarcompra == False:
    print("Seleccione el estilo de zapatillas:")
    print("1. Deportivas")
    print("2. Casuales")
    print("3. Finalizar compra")

    opcion_estilo = input("Ingrese una opción (1-3): ")
    
    if opcion_estilo == "1":
        print("Zapatillas Deportivas disponibles:")
        print("1. Nike Air Max - $150000")
        print("2. Adidas Ultraboost - $180000")
        print("3. Puma RS-X - $130000")
        
        opcion_producto = input("Seleccione el producto que desea comprar (1-3): ")
        if opcion_producto == "1":
            talle = input("Ingrese la talle (39 o 41): ")
            if talle == "39":
                nike_air_max_t_39 += 1
                precio_de_la_compra += 150000
                num_de_compras += 1
                print("Has agregado Nike Air Max talle 39 a tu compra.")
            elif talle == "41":
                nike_air_max_t_41 += 1
                precio_de_la_compra += 150000
                num_de_compras += 1
                print("Has agregado Nike Air Max talle 41 a tu compra.")
            else:
                print("Talle no disponible.")
        elif opcion_producto == "2":
            talle = input("Ingrese la talle (39 o 41): ")
            if talle == "39":
                adidas_ultraboost_t_39 += 1
                precio_de_la_compra += 180000
                num_de_compras += 1
                print("Has agregado Adidas Ultraboost talle 39 a tu compra.")
            elif talle == "41":
                adidas_ultraboost_t_41 += 1
                precio_de_la_compra += 180000
                num_de_compras += 1
                print("Has agregado Adidas Ultraboost talle 41 a tu compra.")
            else:
                print("Talle no disponible.")
        elif opcion_producto == "3":
            talle = input("Ingrese la talle (39 o 41): ")
            if talle == "39":
                puma_rsx_t_39 += 1
                precio_de_la_compra += 130000
                num_de_compras += 1
                print("Has agregado Puma RS-X talle 39 a tu compra.")
            elif talle == "41":
                puma_rsx_t_41 += 1
                precio_de_la_compra += 130000
                num_de_compras += 1
                print("Has agregado Puma RS-X talle 41 a tu compra.")
            else:
                print("Talle no disponible.")
        else:
            print("Opción no válida.")
            
    elif opcion_estilo == "2":
        print("Zapatillas Casuales disponibles:")
        print("1. Vans Old Skool - $90000")
        print("2. Converse All Star - $85000")
        print("3. Converse Jack Purcell - $95000")
        
        opcion_producto = input("Seleccione el producto que desea comprar (1-3): ")
        if opcion_producto == "1":
            talle = input("Ingrese la talle (39 o 41): ")
            if talle == "39":
                vans_old_skool_t_39 += 1
                precio_de_la_compra += 90000
                num_de_compras += 1
                print("Has agregado Vans Old Skool talle 39 a tu compra.")
            elif talle == "41":
                vans_old_skool_t_41 += 1
                precio_de_la_compra += 90000
                num_de_compras += 1
                print("Has agregado Vans Old Skool talle 41 a tu compra.")
            else:
                print("Talle no disponible.")
        elif opcion_producto == "2":
            talle = input("Ingrese la talle (39 o 41): ")
            if talle == "39":
                converse_all_star_t_39 += 1
                precio_de_la_compra += 85000
                num_de_compras += 1
                print("Has agregado Converse All Star talle 39 a tu compra.")
            elif talle == "41":
                converse_all_star_t_41 += 1
                precio_de_la_compra += 85000
                num_de_compras += 1
                print("Has agregado Converse All Star talle 41 a tu compra.")
            else:
                print("Talle no disponible.")
        elif opcion_producto == "3":
            talle = input("Ingrese la talle (39 o 41): ")
            if talle == "39":
                converse_jack_purcell_t_39 += 1
                precio_de_la_compra += 95000
                num_de_compras += 1
                print("Has agregado Converse Jack Purcell talle 39 a tu compra.")
            elif talle == "41":
                converse_jack_purcell_t_41 += 1
                precio_de_la_compra += 95000
                num_de_compras += 1
                print("Has agregado Converse Jack Purcell talle 41 a tu compra.")
            else:
                print("Talle no disponible.")
        else:
            print("Opción no válida.")
            
    elif opcion_estilo == "3":
        finalizarcompra = True
    
    else:
        print("Opción no válida.")

### Precio promedio de las compras
precio_promedio = precio_de_la_compra / num_de_compras
precio_promedio = round(precio_promedio, 2)
print("El precio promedio por par de zapatillas es de", precio_promedio, "pesos.")

### Porcentaje de cada marca vendida
total_deportivas = nike_air_max_t_39 + nike_air_max_t_41 + adidas_ultraboost_t_39 + adidas_ultraboost_t_41 + puma_rsx_t_39 + puma_rsx_t_41
total_casuales = vans_old_skool_t_39 + vans_old_skool_t_41 + converse_all_star_t_39 + converse_all_star_t_41 + converse_jack_purcell_t_39 + converse_jack_purcell_t_41
total_vendido = total_deportivas + total_casuales

porcentaje_deportivas = (total_deportivas / total_vendido) * 100
porcentaje_casuales = (total_casuales / total_vendido) * 100
print("Del total de las zapatillas compradas: El porcentaje de zapatillas deportivas es del", porcentaje_deportivas, "% y el porcentaje de zapatillas casuales es del", porcentaje_casuales, "%.")

### Finalizar compra
if num_de_compras >= 3:
    precio_de_la_compra *= 0.9  # Aplica un 10% de descuento
    print("Se ha aplicado un descuento del 10% al precio de las zapatillas por comprar 3 o más pares.")
    print("El nuevo precio de la compra es de", precio_de_la_compra, "pesos.")

### Envio (retiro por el local o envío a domicilio)
opcion_envio = input("¿Desea retirar su compra por el local o prefiere envío a domicilio? (retirar/enviar): ").lower()
while opcion_envio != "retirar" and opcion_envio != "enviar":
    if opcion_envio == "retirar":
        print("Ha seleccionado retirar su compra por el local. Gracias por su compra.")
    elif opcion_envio == "enviar":
        print("Ha seleccionado envío a domicilio. Procederemos a calcular el costo de envío.")
        if barrio_del_cliente == "Palermo" or barrio_del_cliente == "Recoleta" or barrio_del_cliente == "San Isidro" or barrio_del_cliente == "Nordelta" or barrio_del_cliente == "Belgrano":
            print("El envío es gratuito para su barrio.")
        elif cliente_esta_en_caba == "si":
            precio_del_envio = 5000
            precio_de_la_compra += precio_del_envio
            print("Se ha aplicado un recargo de $5000 por envío a CABA.")
        elif cliente_esta_en_gba == "si":
            precio_del_envio = 8000
            precio_de_la_compra += precio_del_envio
            print("Se ha aplicado un recargo de $8000 por envío a GBA.")
        elif cliente_esta_en_bs_as == "si":
            precio_del_envio = 12000
            precio_de_la_compra += precio_del_envio
            print("Se ha aplicado un recargo de $12000 por envío a Provincia de Buenos Aires.")
        elif cliente_esta_en_arg == "si":
            precio_del_envio = 20000
            precio_de_la_compra += precio_del_envio
            print("Se ha aplicado un recargo de $20000 por envío afuera de la Provincia de Buenos Aires.")
        else:
            precio_del_envio = 80000
            precio_de_la_compra += precio_del_envio
            print("Se ha aplicado un recargo de $80000 por envío internacional.")
    print("Opción no válida. Por favor, seleccione 'retirar' o 'enviar'.")
    opcion_envio = input("¿Desea retirar su compra por el local o prefiere envío a domicilio? (retirar/enviar): ").lower()
    
print("El total de su compra es de", precio_de_la_compra, "pesos.")

### Medio de pago
medio_de_pago = input("Seleccione el medio de pago (efectivo/debito/crédito/bitcoin): ").lower()
while medio_de_pago != "efectivo" and medio_de_pago != "debito" and medio_de_pago != "credito" and medio_de_pago != "bitcoin":
    print("Medio de pago no válido. Por favor, seleccione entre efectivo, débito, crédito o bitcoin.")
    medio_de_pago = input("Seleccione el medio de pago (efectivo/debito/crédito/bitcoin): ").lower()
    
if medio_de_pago == "efectivo":
    print("Ha seleccionado pagar en efectivo. Gracias por su compra.")
elif medio_de_pago == "debito":
    print("Ha seleccionado pagar con débito. Gracias por su compra.")
elif medio_de_pago == "crédito":
    print("Ha seleccionado pagar con crédito. Gracias por su compra.")
elif medio_de_pago == "bitcoin":
    print("Ha seleccionado pagar con bitcoin. Gracias por su compra.")

### Factura final
'''Se debe emitir una factura final que muestre los datos del negocio, los datos del cliente, los productos/servicios adquiridos y la cantidad, envío en caso que exista, medio de pago, descuento, recargo y precios.'''
print("--- FACTURA FINAL ---")

print("Datos del negocio:")
print("Nombre del negocio:", nombre_del_negocio)
print("Dirección del negocio:", direccion_del_negocio)
print("CUIT del negocio:", cuit_del_negocio)

print("Datos del cliente:")
print("Nombre del cliente:", nombre_del_cliente)
print("DNI del cliente:", dni_del_cliente)

print("Productos adquiridos:")
if nike_air_max_t_39 > 0:
    print("Nike Air Max talle 39 - Cantidad:", nike_air_max_t_39, "precio unitario: $150000", "subtotal: $", nike_air_max_t_39 * 150000)
if nike_air_max_t_41 > 0:
    print("Nike Air Max talle 41 - Cantidad:", nike_air_max_t_41, "precio unitario: $150000", "subtotal: $", nike_air_max_t_41 * 150000)
if adidas_ultraboost_t_39 > 0:
    print("Adidas Ultraboost talle 39 - Cantidad:", adidas_ultraboost_t_39, "precio unitario: $180000", "subtotal: $", adidas_ultraboost_t_39 * 180000)
if adidas_ultraboost_t_41 > 0:
    print("Adidas Ultraboost talle 41 - Cantidad:", adidas_ultraboost_t_41, "precio unitario: $180000", "subtotal: $", adidas_ultraboost_t_41 * 180000)
if puma_rsx_t_39 > 0:
    print("Puma RS-X talle 39 - Cantidad:", puma_rsx_t_39, "precio unitario: $130000", "subtotal: $", puma_rsx_t_39 * 130000)
if puma_rsx_t_41 > 0:
    print("Puma RS-X talle 41 - Cantidad:", puma_rsx_t_41, "precio unitario: $130000", "subtotal: $", puma_rsx_t_41 * 130000)
if vans_old_skool_t_39 > 0:
    print("Vans Old Skool talle 39 - Cantidad:", vans_old_skool_t_39, "precio unitario: $90000", "subtotal: $", vans_old_skool_t_39 * 90000)
if vans_old_skool_t_41 > 0:
    print("Vans Old Skool talle 41 - Cantidad:", vans_old_skool_t_41, "precio unitario: $90000", "subtotal: $", vans_old_skool_t_41 * 90000)
if converse_all_star_t_39 > 0:
    print("Converse All Star talle 39 - Cantidad:", converse_all_star_t_39, "precio unitario: $85000", "subtotal: $", converse_all_star_t_39 * 85000)
if converse_all_star_t_41 > 0:
    print("Converse All Star talle 41 - Cantidad:", converse_all_star_t_41, "precio unitario: $85000", "subtotal: $", converse_all_star_t_41 * 85000)
if converse_jack_purcell_t_39 > 0:
    print("Converse Jack Purcell talle 39 - Cantidad:", converse_jack_purcell_t_39, "precio unitario: $95000", "subtotal: $", converse_jack_purcell_t_39 * 95000)
if converse_jack_purcell_t_41 > 0:
    print("Converse Jack Purcell talle 41 - Cantidad:", converse_jack_purcell_t_41, "precio unitario: $95000", "subtotal: $", converse_jack_purcell_t_41 * 95000)

if num_de_compras >= 3:
    print("Descuento aplicado: 10% por comprar 3 o más pares de zapatillas.")

print("Precio total de la compra: $", precio_de_la_compra)

if opcion_envio == "enviar":
    print("El envío se realizó a:", calle_y_num_del_cliente + ", " + barrio_del_cliente, "por lo que se aplicó el recargo de: $", precio_del_envio)
elif opcion_envio == "retirar":
    print("El cliente retirará su compra por el local.")

print("Medio de pago seleccionado:", medio_de_pago)

print("---------------------")