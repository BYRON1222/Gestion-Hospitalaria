import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Paciente } from '../models/paciente.model';

@Injectable({ providedIn: 'root' })
export class PacienteService {
  // Ajusta esta URL si tu backend corre en otro puerto/host
  private apiUrl = 'http://localhost:8000/pacientes/';

  constructor(private http: HttpClient) {}

  listar(): Observable<Paciente[]> {
    return this.http.get<Paciente[]>(this.apiUrl);
  }

  obtener(id: number): Observable<Paciente> {
    return this.http.get<Paciente>(`${this.apiUrl}${id}`);
  }

  crear(paciente: Paciente): Observable<Paciente> {
    return this.http.post<Paciente>(this.apiUrl, paciente);
  }
}
