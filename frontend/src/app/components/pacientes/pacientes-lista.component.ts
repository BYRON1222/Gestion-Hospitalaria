import { Component, OnInit, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PacienteService } from '../../services/paciente.service';
import { Paciente } from '../../models/paciente.model';

@Component({
  selector: 'app-pacientes-lista',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './pacientes-lista.component.html',
})
export class PacientesListaComponent implements OnInit {
  pacientes = signal<Paciente[]>([]);
  cargando = signal(true);
  error = signal('');

  constructor(private pacienteService: PacienteService) {}

  ngOnInit(): void {
    this.pacienteService.listar().subscribe({
      next: (datos) => {
        this.pacientes.set(datos);
        this.cargando.set(false);
      },
      error: () => {
        this.error.set('No se pudo conectar con el backend. ¿Está corriendo en localhost:8000?');
        this.cargando.set(false);
      },
    });
  }
}