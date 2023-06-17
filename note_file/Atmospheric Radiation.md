# Atmospheric Radiation
## Basic Principle
### EM wave
$$\lambda = c/\tilde \nu$$

$$\nu = \tilde \nu /c =1/\lambda$$

where:
$\lambda$: wave length
$\tilde \nu$: frquancy
$\nu$: wave number

In sone cases, both in A.S. and Phy., it is more common to use $\nu$ rather than $\lambda$.
Since that many wave phenomenon occurs in both of the fields, 
the wave number somehow represents the scale of a wave phenomenon.

### Solid Angle
$$\Omega = \frac{\sigma}{r^2}$$
In unit solid angle, no matter how the observer is far away from the radiation source,
the total amount of radiation energy is the same.
If asked for small section of solid angle:
$$d\sigma = (r \; d\phi)(r\; sin\phi \;d\theta)$$

$$\Rightarrow d\Omega = sin\phi d\phi d\theta$$

### Radiative Intensity
* **Intensity**
definition:
$$I_\lambda = \frac{dE_\lambda}{cos\phi \; d\Omega \; d\lambda\; dt\; dA}$$
$cos \theta$ : Only consider the energy that vertically penetrate the area.
$d\Omega$ : all solid angle at area element.
$d\lambda$ : energy emits by spectrum between $\lambda$ and $\lambda + d\lambda$
$dt$ : unit time
$dA$ : unit area

* **Radiation Flux Density**
definition:
$$F_\lambda = \int_\Omega I_\lambda\; cos\phi\; d\Omega$$
Radiative energy penetrate area from all direction for specific wave length.
By using $d\Omega = sin\phi\; d\phi\; d\theta$:
$$F_\lambda = \int_0^{2\pi} \int_0^{\pi/2} I_\lambda(\phi, \theta)\; cos \phi\; sin\phi \; d\phi\; d\theta$$
Considering the intensity is the same in all direction (isotropic radiation), 
then the flux density can be written in:
$$F_\lambda = \pi\; I_\lambda$$

* **Total Flux Density**
definition:
$$F = \int_0^{\infty}\; F_\lambda\; d\lambda$$
integral all the wavelength.

* **Radiative flux**
definition:
$$f = \int_A F\; dA$$
integral all the area.

* **Summarize**


| Quantity     | Symbol | unit              |
| ------------ | ------ | ----------------- |
| Energy       | $E$    | $J$               |
| Flux         | $f$    | $W$               |
| Flux density | $F$    | $W/m^2$           |
| Intensity    | $I$    | $W/(m^2\cdot sr)$ |


### Extinction Process
* **Scattering**
    1. **definition** 
    a method to transfer EM wave, particles absorb radiation and transfer it to every direction.
    Within the process, it can be seperated into two process: absorption and re-radiate.
    2. **Ways of Scattering**
    There are many ways to scatter EM wave, which is determined by the ratio of the radius of particle and wavelength.
    More info of this will be discussed in chapter 3.
    3. **Extinction cross section & extinction coefficient**
        + extinction cross section ($\sigma$)
    energy that is removed by the particle.
    $$\sigma = \frac{f}{F_0}$$
    where $f$ is energy after medium, $F_0$ is energy before medium.
        + extinction coefficient ($\beta$)
    $$\beta = \sigma*n$$
    where $n$ is number density of particle
    
            These two properties are super important in follow chapter, keep their definition and physical meaning in mind. 
    


