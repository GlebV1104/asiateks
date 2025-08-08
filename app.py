import os
from flask import Flask, render_template, send_from_directory , request

application = Flask(__name__)


# Sample product data for testing – a single product reused everywhere
products_data = [
    {
        "id": 1,
       "name": "ЛСП(1*1)_70/30_220/120_П_зеленый",
        "title": "Лён страйп-перкаль пестроткань",
        "images": ["assets/catalog/desktop-catalog/1/1.jpg", "assets/catalog/desktop-catalog/1/2.jpg", "assets/catalog/desktop-catalog/1/3.jpg", "assets/catalog/desktop-catalog/1/4.jpg", "assets/catalog/desktop-catalog/1/5.jpg", "assets/catalog/desktop-catalog/1/6.jpg"],
        "description": "Хлопок 70% Лён 30%; зеленый",
        "detailed_description": [70, 30],
        "price": [400, 380],
        "specifications": [220, 120],
        "tags": ["страйп", "перкаль", "пестроткань"],
        "product_description": "Лён стрейп-перкаль пестроткань – это натуральная ткань в тонкую полоску, созданную за счёт переплетения нитей разных оттенков. Она плотная, но дышащая, с матовой поверхностью. Отлично подходит для пошива стильной одежды (рубашки, платья, брюки), домашнего текстиля (скатерти, шторы) и декора. Прочная, экологичная и приятная на ощупь – идеальный выбор для ценителей натуральных материалов." } ,
    {
        "id": 2,
       "name": "ЛСП(2,5*0,5)_80/20_220/120",
        "title": "Лён страйп-перкаль ",
        "images": ["assets/catalog/desktop-catalog/2/1.jpg", "assets/catalog/desktop-catalog/3/2.jpg", "assets/catalog/desktop-catalog/2/3.jpg", "assets/catalog/desktop-catalog/2/4.jpg", "assets/catalog/desktop-catalog/2/5.jpg", "assets/catalog/desktop-catalog/2/6.jpg"],
        "description": "Хлопок 80% Лён 20%;натуральный",
        "detailed_description": [80, 20],
        "price": [360, 340],
        "specifications": [220, 120],
        "tags": ["страйп", "перкаль"],
        "product_description":"Лён стрейп-перкаль – это натуральная ткань с выраженной полосатой текстурой, созданной за счёт контрастного переплетения нитей. Плотная, но лёгкая, она обладает природной прочностью, хорошо пропускает воздух и приятна телу. Благодаря благородной фактуре идеально подходит для пошива элегантной одежды (рубашки, платья, костюмы), стильного домашнего текстиля (покрывала, шторы, скатерти) и декоративных элементов. Экологичная, износостойкая и тактильно приятная – отличный выбор для тех, кто любит натуральные ткани с характером."} ,
    {
        "id": 3,
       "name": "ЛСП(0,5*0,5)_70/30_220/120_П_зеленый",
        "title": "Лён страйп-перкаль пестроткань",
        "images": ["assets/catalog/desktop-catalog/3/1.jpg", "assets/catalog/desktop-catalog/3/2.jpg", "assets/catalog/desktop-catalog/3/3.jpg", "assets/catalog/desktop-catalog/3/4.jpg", "assets/catalog/desktop-catalog/3/5.jpg", "assets/catalog/desktop-catalog/3/6.jpg"],
        "description": "Хлопок 70% Лён 30%; зеленый",
        "detailed_description": [70, 30],
        "price": [400, 380],
        "specifications": [220, 120],
        "tags": ["страйп", "перкаль", "пестроткань"],
        "product_description": "Лён стрейп-перкаль пестроткань – это натуральная ткань в тонкую полоску, созданную за счёт переплетения нитей разных оттенков. Она плотная, но дышащая, с матовой поверхностью. Отлично подходит для пошива стильной одежды (рубашки, платья, брюки), домашнего текстиля (скатерти, шторы) и декора. Прочная, экологичная и приятная на ощупь – идеальный выбор для ценителей натуральных материалов." } ,
    {
        "id": 5,
       "name": "ЛП_70/30_220/120_П_poseidon",
        "title": "Лён перкаль пестроткань",
        "images": ["assets/catalog/desktop-catalog/5/1.jpg", "assets/catalog/desktop-catalog/5/2.jpg", "assets/catalog/desktop-catalog/5/3.jpg", "assets/catalog/desktop-catalog/5/4.jpg", "assets/catalog/desktop-catalog/5/5.jpg", "assets/catalog/desktop-catalog/5/6.jpg"],
        "description": "Хлопок 70% Лён 30%, poseidon",
        "detailed_description": [70, 30],
        "price": [400, 380],
        "specifications": [220, 120],
        "tags": ["перкаль", "пестроткань"],
        "product_description": "Лён перкаль пестротканый – это натуральная ткань с интересной текстурой, которая получается за счет переплетения разноцветных нитей. Она легкая, но при этом достаточно плотная и прочная. Ткань приятна к телу, хорошо пропускает воздух и не вызывает раздражения, что делает ее идеальной для одежды – платьев, сарафанов, рубашек и блузок. Также из нее получаются отличные постельное белье, скатерти, салфетки и шторы. Благодаря натуральному составу и интересной фактуре, этот материал – отличный выбор для тех, кто ценит экологичность, комфорт и стиль в повседневной жизни." } ,
    {
        "id": 6,
       "name": "ЛП_70/30_220/120_П_зеленый",
        "title": "Лён перкаль пестроткань",
        "images": ["assets/catalog/desktop-catalog/6/1.jpg", "assets/catalog/desktop-catalog/6/2.jpg", "assets/catalog/desktop-catalog/6/3.jpg", "assets/catalog/desktop-catalog/6/4.jpg", "assets/catalog/desktop-catalog/6/5.jpg", "assets/catalog/desktop-catalog/6/6.jpg"],
        "description": "Хлопок 70% Лён 30%, зеленый",
        "detailed_description": [70, 30],
        "price": [400, 380],
        "specifications": [220, 120],
        "tags": ["перкаль", "пестроткань"],
        "product_description": "Лён перкаль пестротканый – это натуральная ткань с интересной текстурой, которая получается за счет переплетения разноцветных нитей. Она легкая, но при этом достаточно плотная и прочная. Ткань приятна к телу, хорошо пропускает воздух и не вызывает раздражения, что делает ее идеальной для одежды – платьев, сарафанов, рубашек и блузок. Также из нее получаются отличные постельное белье, скатерти, салфетки и шторы. Благодаря натуральному составу и интересной фактуре, этот материал – отличный выбор для тех, кто ценит экологичность, комфорт и стиль в повседневной жизни." } ,
    {
        "id": 7,
       "name": "ЛСП(1*1)_80/20_220/120",
        "title": "Лён страйп-перкаль ",
        "images": ["assets/catalog/desktop-catalog/7/1.jpg", "assets/catalog/desktop-catalog/7/2.jpg", "assets/catalog/desktop-catalog/7/3.jpg", "assets/catalog/desktop-catalog/7/4.jpg", "assets/catalog/desktop-catalog/7/5.jpg", "assets/catalog/desktop-catalog/7/6.jpg"],
        "description": "Хлопок 80% Лён 20%;натуральный",
        "detailed_description":[80, 20],
        "price": [360, 340],
        "specifications":[220 , 120],
        "tags": ["страйп", "перкаль"],
        "product_description":"Лён стрейп-перкаль – это натуральная ткань с выраженной полосатой текстурой, созданной за счёт контрастного переплетения нитей. Плотная, но лёгкая, она обладает природной прочностью, хорошо пропускает воздух и приятна телу. Благодаря благородной фактуре идеально подходит для пошива элегантной одежды (рубашки, платья, костюмы), стильного домашнего текстиля (покрывала, шторы, скатерти) и декоративных элементов. Экологичная, износостойкая и тактильно приятная – отличный выбор для тех, кто любит натуральные ткани с характером." } ,
    {
        "id": 8,
       "name": "ЛП_70/30_220/120_П_langustina",
        "title": "Лён перкаль пестроткань",
        "images": ["assets/catalog/desktop-catalog/8/1.jpg", "assets/catalog/desktop-catalog/8/2.jpg", "assets/catalog/desktop-catalog/8/3.jpg", "assets/catalog/desktop-catalog/8/4.jpg", "assets/catalog/desktop-catalog/8/5.jpg", "assets/catalog/desktop-catalog/8/6.jpg"],
        "description": "Хлопок 70% Лён 30%, langustina",
        "detailed_description": [70, 30],
        "price": [400, 380],
        "specifications": [220, 120],
        "tags": ["перкаль", "пестроткань"],
        "product_description": "Лён перкаль пестротканый – это натуральная ткань с интересной текстурой, которая получается за счет переплетения разноцветных нитей. Она легкая, но при этом достаточно плотная и прочная. Ткань приятна к телу, хорошо пропускает воздух и не вызывает раздражения, что делает ее идеальной для одежды – платьев, сарафанов, рубашек и блузок. Также из нее получаются отличные постельное белье, скатерти, салфетки и шторы. Благодаря натуральному составу и интересной фактуре, этот материал – отличный выбор для тех, кто ценит экологичность, комфорт и стиль в повседневной жизни." } ,
    {
        "id": 9,
       "name": "ЛП_70/30_220/120_П_mocha mousse",
        "title": "Лён перкаль пестроткань",
        "images": ["assets/catalog/desktop-catalog/9/1.jpg", "assets/catalog/desktop-catalog/9/2.jpg", "assets/catalog/desktop-catalog/9/3.jpg", "assets/catalog/desktop-catalog/9/4.jpg", "assets/catalog/desktop-catalog/9/5.jpg", "assets/catalog/desktop-catalog/9/6.jpg"],
        "description": "Хлопок 70% Лён 30%, mocha mousse",
        "detailed_description": [70, 30],
        "price": [400, 380],
        "specifications": [220, 120],
        "tags": ["перкаль", "пестроткань"],
        "product_description": "Лён перкаль пестротканый – это натуральная ткань с интересной текстурой, которая получается за счет переплетения разноцветных нитей. Она легкая, но при этом достаточно плотная и прочная. Ткань приятна к телу, хорошо пропускает воздух и не вызывает раздражения, что делает ее идеальной для одежды – платьев, сарафанов, рубашек и блузок. Также из нее получаются отличные постельное белье, скатерти, салфетки и шторы. Благодаря натуральному составу и интересной фактуре, этот материал – отличный выбор для тех, кто ценит экологичность, комфорт и стиль в повседневной жизни." } ,
    {
        "id": 10,
       "name": "ЛСК(1*1)_80/20_150/150",
        "title": "Лён страйп классический",
        "images": ["assets/catalog/desktop-catalog/10/1.jpg", "assets/catalog/desktop-catalog/10/2.jpg", "assets/catalog/desktop-catalog/10/3.jpg", "assets/catalog/desktop-catalog/10/4.jpg", "assets/catalog/desktop-catalog/10/5.jpg", "assets/catalog/desktop-catalog/10/6.jpg"],
        "description": "Хлопок 80% Лён 20%, натуральный",
        "detailed_description": [80, 20],
        "price": [220, 210],
        "specifications": [150, 150],
        "tags": ["классический", "страйп"],
        "product_description": "Лен-страйп классический Ткань идеально сочетает в себе лёгкость и прочность. Она обладает отличной воздухопроницаемостью, хорошо впитывает влагу и быстро высыхает, обеспечивая комфорт в жаркую погоду. Лен придаёт ткани долговечность, элегантность, а также приятную структуру.Лен-страйп классический идеально подходит для летней одежды — платьев, блузок, рубашек и лёгких брюк. Также из этой ткани часто изготавливают текстиль для дома: скатерти, салфетки и постельное бельё." } ,
    {
        "id": 11,
       "name": "ЛСП(2,5*0,5)_70/30_220/120_П_poseidon",
        "title": "Лён страйп-перкаль пестроткань",
        "images": ["assets/catalog/desktop-catalog/11/1.jpg", "assets/catalog/desktop-catalog/11/2.jpg", "assets/catalog/desktop-catalog/11/3.jpg", "assets/catalog/desktop-catalog/11/4.jpg", "assets/catalog/desktop-catalog/11/5.jpg", "assets/catalog/desktop-catalog/11/6.jpg"],
        "description": "Хлопок 80% Лён 20%, poseidon",
        "detailed_description": [80, 20],
        "price": [220, 210],
        "specifications": [150, 150],
        "tags": ["перкаль", "пестроткань"],

        
"product_description": "Лён стрейп-перкаль пестроткань – это натуральная ткань в тонкую полоску, созданную за счёт переплетения нитей разных оттенков. Она плотная, но дышащая, с матовой поверхностью. Отлично подходит для пошива стильной одежды (рубашки, платья, брюки), домашнего текстиля (скатерти, шторы) и декора. Прочная, экологичная и приятная на ощупь – идеальный выбор для ценителей натуральных материалов." } ,
    {
        "id": 12,
       "name": "ЛСП(1*1)_70/30_220/120_П_poseidon",
        "title": "Лён страйп-перкаль пестроткань",
        "images": ["assets/catalog/desktop-catalog/12/1.jpg", "assets/catalog/desktop-catalog/12/2.jpg", "assets/catalog/desktop-catalog/12/3.jpg", "assets/catalog/desktop-catalog/12/4.jpg", "assets/catalog/desktop-catalog/12/5.jpg", "assets/catalog/desktop-catalog/12/6.jpg"],
        "description": "Хлопок 70% Лён 30%; poseidon",
        "detailed_description": [70, 30],
        "price": [400, 380],
        "specifications": [220, 120],
        "tags": ["страйп", "перкаль", "пестроткань"],
        "product_description": "Лён стрейп-перкаль пестроткань – это натуральная ткань в тонкую полоску, созданную за счёт переплетения нитей разных оттенков. Она плотная, но дышащая, с матовой поверхностью. Отлично подходит для пошива стильной одежды (рубашки, платья, брюки), домашнего текстиля (скатерти, шторы) и декора. Прочная, экологичная и приятная на ощупь – идеальный выбор для ценителей натуральных материалов." } ,
    {
        "id": 13,
       "name": "ЛСП(0,5*0,5)_70/30_220/120_П_poseidon",
        "title": "Лён страйп-перкаль пестроткань",
        "images": ["assets/catalog/desktop-catalog/13/1.jpg", "asets/catalog/desktop-catalog/13/2.jpg", "assets/catalog/desktop-catalog/13/3.jpg", "assets/catalog/desktop-catalog/13/4.jpg", "assets/catalog/desktop-catalog/13/5.jpg", "assets/catalog/desktop-catalog/13/6.jpg"],
        "description": "Хлопок 70% Лён 30%; poseidon",
        "detailed_description": [70, 30],
        "price": [400, 380],
        "specifications": [220, 120],
        "tags": ["страйп", "перкаль", "пестроткань"],
        "product_description": "Лён стрейп-перкаль пестроткань – это натуральная ткань в тонкую полоску, созданную за счёт переплетения нитей разных оттенков. Она плотная, но дышащая, с матовой поверхностью. Отлично подходит для пошива стильной одежды (рубашки, платья, брюки), домашнего текстиля (скатерти, шторы) и декора. Прочная, экологичная и приятная на ощупь – идеальный выбор для ценителей натуральных материалов." } ,
    {
        "id": 14,
       "name": "ЛР_60/40_150/165_ПВ",
        "title": "Лён рогожка полувар",
        "images": ["assets/catalog/desktop-catalog/14/1.jpg", "assets/catalog/desktop-catalog/14/2.jpg", "assets/catalog/desktop-catalog/14/3.jpg", "assets/catalog/desktop-catalog/14/4.jpg", "assets/catalog/desktop-catalog/14/5.jpg", "assets/catalog/desktop-catalog/14/6.jpg"],
        "description": "Хлопок 60% Лён 40%; натуральный",
        "detailed_description": [60, 40],
        "price": [242, 230],
        "specifications": [150, 165],
        "tags": ["рогожка", "полувар"],
        "product_description": "Лён рогожка полувар — натуральная ткань с выразительной, немного грубоватой текстурой. Благодаря специальной обработке она становится мягче, но остаётся прочной и плотной. Её плюсы — экологичность, воздухопроницаемость, износостойкость и гипоаллергенность. Ткань подходит для штор, скатертей, подушек, покрывал, а также может использоваться в создании одежды в натуральном стиле." } ,
    {
        "id": 15,
       "name": "ЛК_70/30_220/150_ГК_Мокко",
        "title": "Лен классический гладкокрашенный",
        "images": ["assets/catalog/desktop-catalog/15/1.jpg", "assets/catalog/desktop-catalog/15/2.jpg", "assets/catalog/desktop-catalog/15/3.jpg", "assets/catalog/desktop-catalog/15/4.jpg", "assets/catalog/desktop-catalog/15/5.jpg", "assets/catalog/desktop-catalog/15/6.jpg.jpg"],
        "description": "Хлопок 70% Лён 30%; мокко",
        "detailed_description": [70, 30],
        "price": [340, 315],
        "specifications": [220, 150],
        "tags": ["классический", "гладкокрашеный"],
        "product_description": "Лён классический гладкокрашенный — это натуральная ткань с ровной, гладкой текстурой и однородным цветом. Она отличается простотой, элегантностью и приятна на ощупь. Преимущества ткани — экологичность, воздухопроницаемость, прочность и устойчивость к износу. Лён не вызывает аллергию и отлично подходит для ежедневного использования. Классический гладкокрашенный лён широко применяется для пошива штор, скатертей, постельного белья, декоративного текстиля, а также лёгкой одежды в натуральном стиле." } ,
    {
        "id": 16,
       "name": "ЛК_70/30_220/150_ГК_Фисташковый",
        "title": "Лен классический гладкокрашенный",
        "images": ["assets/catalog/desktop-catalog/16/1.jpg", "assets/catalog/desktop-catalog/16/2.jpg", "assets/catalog/desktop-catalog/16/3.jpg", "assets/catalog/desktop-catalog/16/4.jpg", "assets/catalog/desktop-catalog/16/5.jpg", "assets/catalog/desktop-catalog/16/6.jpg"],
        "description": "Хлопок 70% Лён 30%; Фисташковый",
        "detailed_description": [70, 30],
        "price": [340, 315],
        "specifications": [220, 150],
        "tags": ["классический", "гладкокрашеный"],
        "product_description": "Лён классический гладкокрашенный — это натуральная ткань с ровной, гладкой текстурой и однородным цветом. Она отличается простотой, элегантностью и приятна на ощупь. Преимущества ткани — экологичность, воздухопроницаемость, прочность и устойчивость к износу. Лён не вызывает аллергию и отлично подходит для ежедневного использования. Классический гладкокрашенный лён широко применяется для пошива штор, скатертей, постельного белья, декоративного текстиля, а также лёгкой одежды в натуральном стиле." } ,
    {
        "id": 17,
       "name": "ЛК_70/30_220/150_ГК_Пудровая Роза",
        "title": "Лен классический гладкокрашенный",
        "images": ["assets/catalog/desktop-catalog/17/1.jpg", "assets/catalog/desktop-catalog/17/2.jpg", "assets/catalog/desktop-catalog/17/3.jpg", "assets/catalog/desktop-catalog/17/4.jpg", "assets/catalog/desktop-catalog/17/5.jpg", "assets/catalog/desktop-catalog/17/6.jpg"],
        "description": "Хлопок 70% Лён 30%; Пудровая Роза",
        "detailed_description": [70, 30],
        "price": [340, 315],
        "specifications": [220, 150],
        "tags": ["классический", "гладкокрашеный"],
        "product_description": "Лён классический гладкокрашенный — это натуральная ткань с ровной, гладкой текстурой и однородным цветом. Она отличается простотой, элегантностью и приятна на ощупь. Преимущества ткани — экологичность, воздухопроницаемость, прочность и устойчивость к износу. Лён не вызывает аллергию и отлично подходит для ежедневного использования. Классический гладкокрашенный лён широко применяется для пошива штор, скатертей, постельного белья, декоративного текстиля, а также лёгкой одежды в натуральном стиле." } ,
    {
        "id": 18,
       "name": "ЛК_70/30_150/140_H_веточки бель",
        "title": "Лён классика набивная",
        "images": ["assets/catalog/desktop-catalog/18/1.jpg", "assets/catalog/desktop-catalog/18/2.jpg", "assets/catalog/desktop-catalog/18/3.jpg", "assets/catalog/desktop-catalog/18/4.jpg", "assets/catalog/desktop-catalog/18/5.jpg", "assets/catalog/desktop-catalog/18/6.jpg"],
        "description": "Хлопок 70% Лён 30%; веточки бель",
        "detailed_description": [70, 30],
        "price": [255, 240],
        "specifications": [150, 140],
        "tags": ["классика", "набивная"],
        "product_description": "Лён классика набивная — натуральная ткань с гладкой поверхностью и мягкой текстурой. Благодаря специальной обработке она остаётся прочной, приятной на ощупь и хорошо держит форму. Среди её преимуществ — экологичность, воздухопроницаемость, износостойкость и гипоаллергенность. Такая ткань удобна в использовании и подходит для повседневных задач. Лён набивной отлично подойдёт для штор, скатертей, подушек, домашнего текстиля, а также для пошива лёгкой и комфортной одежды." } ,
    {
        "id": 20,
       "name": "ЛСП(0,5*0,5)_80/20_220/120",
        "title": "Лён страйп-перкаль ",
        "images": ["assets/catalog/desktop-catalog/20/1.jpg", "assets/catalog/desktop-catalog/20/2.jpg", "assets/catalog/desktop-catalog/20/3.jpg", "assets/catalog/desktop-catalog/20/4.jpg", "assets/catalog/desktop-catalog/20/5.jpg", "assets/catalog/desktop-catalog/20/6.jpg"],
        "description": "Хлопок 80% Лён 20%; натуральный",
        "detailed_description": [80, 20],
        "price": [360, 340],
        "specifications": [220, 120],
        "tags": ["страйп", "перкаль"],
        "product_description": "Лён стрейп-перкаль – это натуральная ткань с выраженной полосатой текстурой, созданной за счёт контрастного переплетения нитей. Плотная, но лёгкая, она обладает природной прочностью, хорошо пропускает воздух и приятна телу. Благодаря благородной фактуре идеально подходит для пошива элегантной одежды (рубашки, платья, костюмы), стильного домашнего текстиля (покрывала, шторы, скатерти) и декоративных элементов. Экологичная, износостойкая и тактильно приятная – отличный выбор для тех, кто любит натуральные ткани с характером." } ,
    {
        "id": 22,
       "name": "ЛК_70/30_150/140_ПВ",
        "title": "Лён классический полувар",
        "images": ["assets/catalog/desktop-catalog/22/1.jpg", "assets/catalog/desktop-catalog/22/2.jpg", "assets/catalog/desktop-catalog/22/3.jpg", "assets/catalog/desktop-catalog/22/4.jpg", "assets/catalog/desktop-catalog/22/5.jpg", "assets/catalog/desktop-catalog/22/6.jpg"],
        "description": "Хлопок 70% Лён 30%;натуральный",
        "detailed_description": [70, 30],
        "price": [220, 210],
        "specifications": [150, 140],
        "tags": ["классический", "полувар"],
        "product_description": "Лён классический полувар — натуральная ткань средней плотности с гладкой поверхностью. Благодаря полуварке материал становится мягче, приятнее на ощупь, но сохраняет прочность и структуру. Преимущества: экологичность, воздухопроницаемость, гипоаллергенность, износостойкость. Подходит для пошива штор, скатертей, подушек, домашнего текстиля и лёгкой одежды." } ,
    {
        "id": 23,
       "name": "ЛК_70/30_220/150_ГК_Фиолетовый",
        "title": "Лен классический гладкокрашенный",
        "images": ["assets/catalog/desktop-catalog/23/1.jpg", "assets/catalog/desktop-catalog/23/2.jpg", "assets/catalog/desktop-catalog/23/3.jpg", "assets/catalog/desktop-catalog/23/4.jpg", "assets/catalog/desktop-catalog/23/5.jpg", "assets/catalog/desktop-catalog/23/6.jpg"],
        "description": "Хлопок 70% Лён 30%; фиолетовый",
        "detailed_description": [70, 30],
        "price": [340, 315],
        "specifications": [220, 150],
        "tags": ["классический", "гладкокрашеный"],
        "product_description": "Лён классический гладкокрашенный — это натуральная ткань с ровной, гладкой текстурой и однородным цветом. Она отличается простотой, элегантностью и приятна на ощупь. Преимущества ткани — экологичность, воздухопроницаемость, прочность и устойчивость к износу. Лён не вызывает аллергию и отлично подходит для ежедневного использования. Классический гладкокрашенный лён широко применяется для пошива штор, скатертей, постельного белья, декоративного текстиля, а также лёгкой одежды в натуральном стиле." } ,
    {
        "id": 25,
       "name": "ЛСП(2,5*0,5)_70/30_220/120_П_зеленый",
        "title": "Лён страйп-перкаль пестроткань",
        "images": ["assets/catalog/desktop-catalog/25/1.jpg", "assets/catalog/desktop-catalog/25/2.jpg", "assets/catalog/desktop-catalog/25/3.jpg", "assets/catalog/desktop-catalog/25/4.jpg", "assets/catalog/desktop-catalog/25/5.jpg", "assets/catalog/desktop-catalog/25/6.jpg"],
        "description": "Хлопок 70% Лён 30%; зеленый",
        "detailed_description": [70, 30],
        "price": [400, 380],
        "specifications": [220, 120],
        "tags": ["страйп", "перкаль", "пестроткань"],
        "product_description": "Лён стрейп-перкаль пестроткань – это натуральная ткань в тонкую полоску, созданную за счёт переплетения нитей разных оттенков. Она плотная, но дышащая, с матовой поверхностью. Отлично подходит для пошива стильной одежды (рубашки, платья, брюки), домашнего текстиля (скатерти, шторы) и декора. Прочная, экологичная и приятная на ощупь – идеальный выбор для ценителей натуральных материалов." } ,
    {
        "id": 28,
       "name": "ЛК_70/30_220/150_ПВ",
        "title": "Лён классический полувар",
        "images": ["assets/catalog/desktop-catalog/28/1.jpg", "assets/catalog/desktop-catalog/28/2.jpg", "assets/catalog/desktop-catalog/28/3.jpg", "assets/catalog/desktop-catalog/28/4.jpg", "assets/catalog/desktop-catalog/28/5.jpg", "assets/catalog/desktop-catalog/28/6.jpg"],
        "description": "Хлопок 70% Лён 30%;натуральный",
        "detailed_description": [70, 30],
        "price": [320, 305],
        "specifications": [220, 150],
        "tags": ["классический", "полувар"],
        "product_description": "Лён классический полувар — натуральная ткань средней плотности с гладкой поверхностью. Благодаря полуварке материал становится мягче, приятнее на ощупь, но сохраняет прочность и структуру. Преимущества: экологичность, воздухопроницаемость, гипоаллергенность, износостойкость. Подходит для пошива штор, скатертей, подушек, домашнего текстиля и лёгкой одежды." } ,
    {
        "id": 30,
       "name": "ЛК_70/30_150/140_H_листочки бель",
        "title": "Лён классика набивная",
        "images": ["assets/catalog/desktop-catalog/30/1.jpg", "assets/catalog/desktop-catalog/30/2.jpg", "assets/catalog/desktop-catalog/30/3.jpg", "assets/catalog/desktop-catalog/30/4.jpg", "assets/catalog/desktop-catalog/30/5.jpg", "assets/catalog/desktop-catalog/30/6.jpg"],
        "description": "Хлопок 70% Лён 30%; веточки бель",
        "detailed_description": [70, 30],
        "price": [255, 240],
        "specifications": [150, 140],
        "tags": ["классика", "набивная"],
        "product_description": "Лён классика набивная — натуральная ткань с гладкой поверхностью и мягкой текстурой. Благодаря специальной обработке она остаётся прочной, приятной на ощупь и хорошо держит форму. Среди её преимуществ — экологичность, воздухопроницаемость, износостойкость и гипоаллергенность. Такая ткань удобна в использовании и подходит для повседневных задач. Лён набивной отлично подойдёт для штор, скатертей, подушек, домашнего текстиля, а также для пошива лёгкой и комфортной одежды." } ,
    {
        "id": 33,
       "name": "ЛК_70/30_220/150_ГК_молочный зефир",
        "title": "Лен классический гладкокрашенный",
        "images": ["assets/catalog/desktop-catalog/33/1.jpg", "assets/catalog/desktop-catalog/33/2.jpg", "assets/catalog/desktop-catalog/33/3.jpg", "assets/catalog/desktop-catalog/33/4.jpg", "assets/catalog/desktop-catalog/33/5.jpg", "assets/catalog/desktop-catalog/33/6.jpg"],
        "description": "Хлопок 70% Лён 30%; молочный зефир",
        "detailed_description": [70, 30],
        "price": [340, 315],
        "specifications": [220, 150],
        "tags": ["классический", "гладкокрашеный"],
        "product_description": "Лён классический гладкокрашенный — это натуральная ткань с ровной, гладкой текстурой и однородным цветом. Она отличается простотой, элегантностью и приятна на ощупь. Преимущества ткани — экологичность, воздухопроницаемость, прочность и устойчивость к износу. Лён не вызывает аллергию и отлично подходит для ежедневного использования. Классический гладкокрашенный лён широко применяется для пошива штор, скатертей, постельного белья, декоративного текстиля, а также лёгкой одежды в натуральном стиле." } ,
    {
        "id": 37,
       "name": "ЛК_70/30_220/150_ГК_Графит",
        "title": "Лен классический гладкокрашенный",
        "images": ["assets/catalog/desktop-catalog/37/1.jpg", "assets/catalog/desktop-catalog/37/2.jpg", "assets/catalog/desktop-catalog/37/3.jpg", "assets/catalog/desktop-catalog/37/4.jpg", "assets/catalog/desktop-catalog/37/5.jpg", "assets/catalog/desktop-catalog/37/6.jpg"],
        "description": "Хлопок 70% Лён 30%; Графит",
        "detailed_description": [70, 30],
        "price": [340, 315],
        "specifications": [220, 150],
        "tags": ["классический", "гладкокрашеный"],
        "product_description": "Лён классический гладкокрашенный — это натуральная ткань с ровной, гладкой текстурой и однородным цветом. Она отличается простотой, элегантностью и приятна на ощупь. Преимущества ткани — экологичность, воздухопроницаемость, прочность и устойчивость к износу. Лён не вызывает аллергию и отлично подходит для ежедневного использования. Классический гладкокрашенный лён широко применяется для пошива штор, скатертей, постельного белья, декоративного текстиля, а также лёгкой одежды в натуральном стиле."}]







@application.route('/products')
def products():
    query = request.args.get('search', '').lower()
    tag_filter = request.args.get('tag', '').lower()

    filtered_products = [
        product for product in products_data
        if (query in product["title"].lower() or query in product["description"].lower())
        and (tag_filter in [t.lower() for t in product.get("tags", [])] if tag_filter else True)
    ]
    
    return render_template('products.html', products=filtered_products, query=query, tag_filter=tag_filter)
@application.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((item for item in products_data if item["id"] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product, products=products_data)
    else:
        return "Product not found", 404
# Render the homepage using home.html
@application.route('/')
def home():
    return render_template('home.html')

# Serve static files from the 'static' folder
@application.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(application.root_path, 'static'), filename)

# Download files from the 'static/files' folder
@application.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory(os.path.join(application.root_path, 'static', 'files'), filename, as_attachment=True)

@application.template_filter('intersect')
def intersect(a, b):
    return list(set(a) & set(b))

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5001 , debug=True)