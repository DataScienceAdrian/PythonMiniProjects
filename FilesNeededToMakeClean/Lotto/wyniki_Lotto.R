library(rvest)
library(dplyr)
library(mailR) #Dziala na 32 bitowej wersji R

Wczytaj_ze_strony = function(){
  lotto_wyniki <- read_html("http://www.lotto.pl/lotto/wyniki-i-wygrane")
  wyniki2 <- html_nodes(lotto_wyniki, ".wynik_lotto") #same wyniki w liczbach
  
  #Lotto
  ostatnie_lotto = wyniki2[1:12]
  html_read = html_text(ostatnie_lotto)

  int_ostatnie_lotto = as.numeric(html_read)
  int_ostatnie_lotto = as.integer(int_ostatnie_lotto)
  
  
  #Lotto Plus
  ostatnie_plus = wyniki2
  html_read_plus = t(html_text(ostatnie_plus))
  
  int_ostatnie_plus = as.numeric(html_read_plus)
  int_ostatnie_plus = t(as.integer(int_ostatnie_plus))
  
  int_ostatnie_plus = int_ostatnie_plus[1,13:18]
  
  
  
  dataLiczby = read.csv('D:/Programowanie/R_Projects/Lotto/liczby.csv',dec = ".",header = F,sep = ';')
  
  moje_liczby = as.integer(dataLiczby[1:6])
  
  
  Lotto = c(int_ostatnie_lotto)
  Plus = c(int_ostatnie_plus)
  Moje = c(moje_liczby)
  
  if(Lotto = Moje){
    zlicz = 0
    zlicz = zlicz +1
    
    
    
  }
  if(Plus = Moje){
    zlicz2 = 0
    zlicz2 = zlicz2 +1
    
    
  }
  
  Moje_Char = toString(Moje)
  Lotto_Char = toString(Lotto)
  
  Plus_Char = toString(Plus)
  zlicz_Char = toString(zlicz)
  zlicz2_Char = toString(zlicz2)
  
 
    Wypisz = paste("Twoje liczby to: ",Moje_Char,
                   "Ostatnie wylosowane liczby to: ",Lotto_Char,
                   "Trafiles",zlicz_Char,"z 6 liczb")
    
    Wypisz_Plus = paste("Twoje liczby w Plusie to: ",Moje_Char,
                        "Ostatnie wylosowane liczby to: ",Lotto_Char,
                        "Trafiles",zlicz_Char,"z 6 liczb")
    
  
  

}

zapisz_do_pliku = function(Wczytaj_ze_strony){
  
  New_Line = cat('\n\n')
  fileConn<-file("Twoje_Wyniki.txt")
  writeLines(paste(Wypisz,New_Line,Wypisz_Plus),fileConn)
  close(fileConn)
  
}


wyslij_maile = function(zapisz_do_pliku,Wczytaj_ze_strony){
  sender <- "amarcinczyk95@gmail.com"
  recipients <- "amarcinczyk95@gmail.com"
  send.mail(from = sender,
            to = recipients,
            subject = "Ostatnie wyniki Lotto z Plusem",
            body = "Wyniki w zalaczniku",
            attach.files = c("Twoje_Wyniki.txt"),
            smtp = list(host.name = "smtp.gmail.com", port = 465, 
                        user.name = "amarcinczyk95@gmail.com",            
                        passwd = "28092004rm", ssl = TRUE),
            authenticate = TRUE,
            send = TRUE)
  
}




library(rJava)

#Plus
ostatni_plus = wyniki2[1:12]

html_text(ostatni_plus)

wyniki_txt.parsed = gsub('\\n', '', wyniki_txt)
wyniki_txt.parsed = gsub('\\([0-9]+\\)', '', wyniki_txt.parsed)
wyniki_txt.parsed = gsub('^ +[0-9]+\\. +', '', wyniki_txt.parsed)
wyniki_txt.parsed = gsub(' +$', '', wyniki_txt.parsed)
