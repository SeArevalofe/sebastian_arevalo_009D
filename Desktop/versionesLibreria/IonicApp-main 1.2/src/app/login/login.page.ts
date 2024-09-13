import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { IonicModule } from '@ionic/angular';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
  standalone: true,
  imports: [IonicModule,RouterLink,CommonModule, FormsModule]
})
export class LoginPage implements OnInit {

 
  email: string = '';
  password: string = '';
 
  
  constructor() { }

  ngOnInit() {
    
  }

}
