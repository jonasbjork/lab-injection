# lab-injection

Lab som visar en injektion.

## Bygga

```console
podman build -t injection:latest .
```

## Köra

```
podman run -it --rm --name injection -p 5000:5000 injection:latest
```

- Öppna sedan webbläsaren och anslut: 127.0.0.1:5000
- Klicka på filerna och gå sedan till adressfältet och ändra `?file=`



