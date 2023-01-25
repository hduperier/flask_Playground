import React from 'react'
import styles from './style';

const App = () => {
    return (<div classname="bg-primary w-full overflow-hidden">
      <div className={'${styles.paddingX} ${styles.flexCenter}'}>
        < div className={'${styles.boxWidth}'}>
          Navbar
        </div>
      </div>
    </div>
  )
}

export default App
