export default function authHeader() {
  var token = localStorage.getItem('token')
  
  if (token != 'undefined') {
    return { Authorization: 'Token ' + token };
  } else {
    return {};
  }
}
