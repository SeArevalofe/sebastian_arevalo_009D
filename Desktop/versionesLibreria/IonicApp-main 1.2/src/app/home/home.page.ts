import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { IonicModule } from '@ionic/angular';
import { RouterModule, Routes } from '@angular/router';

import { addIcons } from 'ionicons';
import { add } from 'ionicons/icons';



@Component({
  selector: 'app-home',
  templateUrl: './home.page.html',
  styleUrls: ['./home.page.scss'],
  standalone: true,
  imports: [ CommonModule, FormsModule, IonicModule,RouterModule]
})
export class HomePage implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
