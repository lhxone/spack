# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAplot(RPackage):
    """Decorate a 'ggplot' with Associated Information.

    For many times, we are not just aligning plots as what 'cowplot' and
    'patchwork' did. Users would like to align associated information that
    requires axes to be exactly matched in subplots, e.g. hierarchical
    clustering with a heatmap. This package provides utilities to aligns
    associated subplots to a main plot at different sides (left, right, top and
    bottom) with axes exactly matched."""

    cran = "aplot"

    version('0.1.6', sha256='7d69d1968bc613d8ceccc05c53362b0f62b632e1c6ef5100c91b65b15afa200c')
    version('0.1.4', sha256='cde9dfc1c6b38e370c1f7338651c37727efa57d52b646fec6b021855809492ac')
    version('0.1.2', sha256='899c4d101ddcedb1eba9803d78cf02288b63de25e2879add8add1165167509f0')

    depends_on('r-ggfun@0.0.4:', type=('build', 'run'), when='@0.1.2:')
    depends_on('r-ggfun@0.0.6:', type=('build', 'run'), when='@0.1.4:')
    depends_on('r-ggplot2', type=('build', 'run'))
    depends_on('r-ggplotify', type=('build', 'run'))
    depends_on('r-patchwork', type=('build', 'run'))
    depends_on('r-magrittr', type=('build', 'run'))

    depends_on('r-yulab-utils', type=('build', 'run'), when='@0.1.2')
