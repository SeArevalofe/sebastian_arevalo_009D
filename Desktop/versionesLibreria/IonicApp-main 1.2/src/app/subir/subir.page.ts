import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { IonicModule } from '@ionic/angular';


@Component({
  selector: 'app-subir',
  templateUrl: './subir.page.html',
  styleUrls: ['./subir.page.scss'],
  standalone: true,
  imports: [ CommonModule, FormsModule, RouterLink, IonicModule]
})
export class SubirPage implements OnInit {
  
  

  titulo: string = '';
  autor: string = '';
  

  constructor() { }

  ngOnInit() {
  }

}
