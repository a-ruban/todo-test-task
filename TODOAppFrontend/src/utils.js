import router from '@/router'

export const errorHandler = function (err) {
  if (err.response) {
    if (err.response.status === 401) {
      localStorage.clear()
      router.push('/login')
      alert('Session expired. Please, login again')
    } else if (![404, 500].includes(err.response.status)) {
      for (let errorField in err.response.data) {
        let errorValues = err.response.data[errorField]
        if (errorField === 'detail') {
          alert(errorValues)
        } else {
          for (let errorMessage of errorValues) {
            let errorText =
            errorField === 'non_field_errors'
              ? errorMessage
              : `${errorField}: ${errorMessage}`
            alert(errorText)
          }
        }
      }
    }
    if (err.response.status === 500) {
      alert('Internal server error.')
    }
  } else {
    console.error(err)
  }
}
