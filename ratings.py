#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ratings_students(ratings):
    status = True
    aprroved = 0
    disapproved = 0
    for r in ratings:
        if r < 13:
            disapproved += 1
        else:
            aprroved += 1
    cant = len(ratings)
    print('Verificando Calificaciones')
    print('Cantidad de Alumnos {0}'.format(cant))
    print('Aprobados: {0} | Desaprobados: {1}'.format(aprroved, disapproved))

students = [12, 15, 19, 20, 11, 5, 13, 7, 12, 15, 15, 17, 18, 20, 20, 2, ]
ratings_students(students)
        
        
