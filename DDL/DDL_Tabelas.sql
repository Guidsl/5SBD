CREATE TABLE "Carga" (
    "order-id" nvarchar(10),
    "order-item-id" nvarchar(10),
    "purchase-date" date,
    "payments-date" date,
    "buyer-email" nvarchar(200),
    "buyer-name" nvarchar(200),
    "cpf" nvarchar(11),
    "buyer-phone-number" nvarchar(20),
    "sku" nvarchar(25),
    "upc" nvarchar(25),
    "product-name" nvarchar(200),
    "quantity-purchased" tinyint,
    "currency" nvarchar(3),
    "item-price" money,
    "ship-service-level" nvarchar(50),
    "ship-address-1" nvarchar(200),
    "ship-address-2" nvarchar(200),
    "ship-address-3" nvarchar(200),
    "ship-city" nvarchar(200),
    "ship-state" nvarchar(200),
    "ship-postal-code" nvarchar(20),
    "ship-country" nvarchar(2)
);
CREATE TABLE "Cliente" (
"id-client" int IDENTITY(1, 1) PRIMARY KEY,
"buyer-email" nvarchar(200),
"buyer-name" nvarchar(200),
"cpf" nvarchar(11),
"buyer-phone-number" nvarchar(20)
);
CREATE TABLE Produto(
"id-product" int IDENTITY(1, 1) PRIMARY KEY,
"sku" nvarchar(25),
"upc" nvarchar(25),
"product-name" nvarchar(200),
"item-price" money
); 
CREATE TABLE Pedidos(
    "id-order" int IDENTITY(1, 1) PRIMARY KEY,
    "order-id-marketplace" nvarchar(10),
    "id-client" int,
    "purchase-date" date,
    "payments-date" date,
    "currency" nvarchar(3),
    "total" money,
    "ship-service-level" nvarchar(50),
    "ship-address-1" nvarchar(200),
    "ship-address-2" nvarchar(200),
    "ship-address-3" nvarchar(200),
    "ship-city" nvarchar(200),
    "ship-state" nvarchar(200),
    "ship-postal-code" nvarchar(20),
    "ship-country" nvarchar(2),
    FOREIGN KEY ("id-client") REFERENCES Cliente("id-client")
); 
CREATE TABLE ItemPedido (
    "id-order" int,
    "id-product" int,
    "quantity" int,
    "order-item-id" nvarchar(10),
    FOREIGN KEY ("id-order")   REFERENCES Pedido  ("id-order"),
    FOREIGN KEY ("id-product") REFERENCES Produto ("id-product")
);

CREATE TABLE Movimento (
	"id-order" int,
	"status" nvarchar (15) DEFAULT 'Processing',
	"compleation-date" date,
	FOREIGN KEY ("id-order") REFERENCES Pedido ("id-order")
	);

CREATE TABLE Estoque (
	"id-product" int,
	"quantity" int,
	FOREIGN KEY ("id-product") REFERENCES Produto ("id-product")
	);
