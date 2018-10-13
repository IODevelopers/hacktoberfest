load arquivo.mat;
size = length(sinal);
janela = 5000;

for i = 1 : 1 : size - janela
  energia(i) = sum(abs(sinal(i:i + janela - 1).^2));
end

acima = find(energia > 250);
acimaVet = acima(2:end) - acima(1: end - 1);
ciclos = length(find(acimaVet > 1)) + 1;

plot(oi);
