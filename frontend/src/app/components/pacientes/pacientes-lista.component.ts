import { Component, OnInit, signal, computed } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MatTableModule } from '@angular/material/table';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatCardModule } from '@angular/material/card';
import { PacienteService } from '../../services/paciente.service';
import { Paciente } from '../../models/paciente.model';

@Component({
  selector: 'app-pacientes-lista',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    MatTableModule,
    MatFormFieldModule,
    MatInputModule,
    MatIconModule,
    MatProgressSpinnerModule,
    MatCardModule,
  ],
  templateUrl: './pacientes-lista.component.html',
  styleUrl: './pacientes-lista.component.css',
})
export class PacientesListaComponent implements OnInit {
  pacientes = signal<Paciente[]>([]);
  cargando = signal(true);
  error = signal('');
  filtro = signal('');

  columnasVisibles = ['nombre', 'apellido', 'documento_identidad', 'telefono'];

  pacientesFiltrados = computed(() => {
    const texto = this.filtro().toLowerCase().trim();
    if (!texto) return this.pacientes();
    return this.pacientes().filter(
      (p) =>
        p.nombre.toLowerCase().includes(texto) ||
        p.apellido.toLowerCase().includes(texto) ||
        p.documento_identidad.toLowerCase().includes(texto)
    );
  });

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

  actualizarFiltro(valor: string): void {
    this.filtro.set(valor);
  }
}