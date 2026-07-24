import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PacientesListaComponent } from './components/pacientes/pacientes-lista.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, PacientesListaComponent],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('frontend');
}