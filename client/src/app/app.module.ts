import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { InformationComponent } from './information/information.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http'; ``

@NgModule({
  declarations: [
    AppComponent,
    InformationComponent

  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
