import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-ahorcado',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './ahorcado.component.html',
  styleUrl: './ahorcado.component.css'
})

export class AhorcadoComponent implements OnInit {
  palabraSecreta: string = '';
  palabraMostrada: string = '';
  intentosRestantes: number = 6;
  letrasIntentadas: string[] = [];
  mensaje: string = '';
  letraIngresada: string = '';

  palabras: string[] = ['ANGULAR', 'JAVASCRIPT', 'COMPONENTE', 'HTML', 'CSS']; 

  ngOnInit(): void {
    this.seleccionarPalabra();
    this.actualizarPalabraMostrada();
  }

  seleccionarPalabra(): void {
    this.palabraSecreta = this.palabras[Math.floor(Math.random() * this.palabras.length)];
  }

  actualizarPalabraMostrada(): void {
    this.palabraMostrada = '';
    for (let letra of this.palabraSecreta) {
      if (this.letrasIntentadas.includes(letra)) {
        this.palabraMostrada += letra + ' ';
      } else {
        this.palabraMostrada += '_ ';
      }
    }
  }

  intentar(letra: string): void {
    if (!this.letrasIntentadas.includes(letra)) {
      this.letrasIntentadas.push(letra);
      if (!this.palabraSecreta.includes(letra)) {
        this.intentosRestantes--;
      }
      this.actualizarPalabraMostrada();
      this.verificarEstadoJuego();
    }
  }

  verificarEstadoJuego(): void {
    if (this.intentosRestantes <= 0) {
      this.mensaje = '¡Perdiste! La palabra era: ' + this.palabraSecreta;
    } else if (this.palabraSecreta === this.palabraMostrada.replace(/ /g, '')) {
      this.mensaje = '¡Ganaste!';
    }
  }

  reiniciarJuego(): void {
    // Reinicia el juego
    this.intentosRestantes = 6;
    this.letrasIntentadas = [];
    this.seleccionarPalabra();
    this.actualizarPalabraMostrada();
    this.mensaje = '';
  }
}