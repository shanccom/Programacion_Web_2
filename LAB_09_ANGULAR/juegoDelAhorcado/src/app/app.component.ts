import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {AhorcadoComponent} from './ahorcado/ahorcado.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, AhorcadoComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'JuegoDelAhorcado';
}
